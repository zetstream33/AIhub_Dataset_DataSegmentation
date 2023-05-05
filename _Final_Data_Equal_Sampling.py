import xml.etree.ElementTree as ET
import glob
import os
import os.path
import shutil
from datetime import datetime


'''LIST VARIABLE'''
ORDER = ['wheelchair','stroller','power_controller','traffic_light_controller','table','kiosk','carrier','dog','fire_hydrant','stop','barricade','bench','chair','bus','bicycle','motorcycle','potted_plant','movable_signage','truck','traffic_light','traffic_sign','bollard','pole','person','tree_trunk','car']
used_img = []
# 'scooter',

'''INT VARIABLE'''
INSTANCE_THRESHOLD = 1700
folder_number = 2480

'''DICTIONARY VARIABLE'''
Class_index = {'bicycle' : 0
    ,'bus':1
    ,'car':2
    ,'carrier':3
    ,'cat':4
    ,'dog':5
    ,'motorcycle':6
    ,'movable_signage':7
    ,'person':8
    ,'scooter':9
    ,'stroller':10
    ,'truck':11
    ,'wheelchair':12
    ,'barricade':13
    ,'bench':14
    ,'bollard':15
    ,'chair':16
    ,'fire_hydrant':17
    ,'kiosk':18
    ,'parking_meter':19
    ,'pole':20
    ,'potted_plant':21
    ,'power_controller':22
    ,'stop':23
    ,'table':24
    ,'traffic_light':25
    ,'traffic_light_controller':26
    ,'traffic_sign':27
    ,'tree_trunk':28} #Class Annotation을 위한 {클래스 이름 : 라벨 넘버} 1:1 대응 Dictionary
Class_num = {} #Instance 개수를 구하기 위한 {인스턴스(클래스) 이름 : 인스턴스(클래스) 갯수} 1:1 대응 Dictionary
                                            #Class_num의 해당되는 int 값들은 전부 0으로 설정되어 있는 상태.
                                            #Class_num은 전역변수로 사용해야 업데이트에 용이함. 함수 인자로 받지 않고 바깥에 그대로 냅둠.

'''STRING VARIABLE'''

location = "/home/zetstream/Dataset/train/"
new_location = "home/zetstream/Dataset_Equal/train/"


location_win = "C:/Users/dldjw/OneDrive/바탕 화면/Test/"
new_location_win = "C:/Users/dldjw/OneDrive/바탕 화면/Test2/"

image_Bbox = "images/Bbox_"
label_Bbox = "labels/Bbox_"

log_dir = "/home/zetstream/Data_equal_Sampling_LOG.txt"
log_dir_win = "C:/Users/dldjw/OneDrive/바탕 화면/Data_equal_Sampling_LOG.txt"

for name in enumerate(Class_index):
    # print(name)
    Class_num[name[1]] = 0


# 우선순위 적용. 인스턴스 개수가 적은 순서로, 오름차순으로 정렬함.
# 크게 3가지 과정이 필요함

# 첫번째 : Order 배열을 순서대로 읽으면서 각 해당되는 값의 box 가 있는 이미지를 찾음

# 두번째 : 이미지를 찾았으면 그 이미지 파일을 옮기고 해당되는 박스의 라벨을 동시에 옮긴 폴더에 생성함.
#         라벨을 생성함과 동시에 Class_num에 그 개수를 업데이트 함. 이때 옮긴 파일의 이름을 used_img 배열에 담음.

# 세번째 : 과정을 반복하다가 정해진 instance_THRESHOLD 개수를 채우면 옮김을 중지. Order의 다음 인스턴스와 Class_num의 그 인스턴스의 개수를 확인.
#                       만약 Class_num(해당되는 인스턴스) < instance_THRESHOLD 이면 그 차이만큼 채움 시작. 이 과정을 반복함.

# 추가적인 사항 : 각 Iteration 마다 Log를 기록하여 txt로 남기면 디버깅 편리할 듯.


def Count_instance_num(Class_num):
    sum = 0
    for i in range(Class_num):
        sum += i[Class_num[1]]
    return sum

def Progress(Order, Threshold):
    for iter, instance_selected in enumerate(Order):
        instance_number = Class_num[instance_selected]
        instance_needed = Threshold - instance_number
        print("{}th iter {} : {}, needed : {}".format(iter+1, instance_selected,instance_number,instance_needed))
        # 각 인스턴스 별로 개수 & 필요 개수 Check

        if instance_needed <= 0:
            print("Instance {} 가 기준치보다 많아 스킵, 다음 iteration 진행.".format(instance_selected)) #이건 총 두번 필요함. 이미지 전체를 훑기전에 한번, 훑으면서도 한번 계속 체크 필요.
        else:
            # 이 else문에 처리하는 코드 작성
            print("Instance {} 가 {}개 모자람. 이미지 추가 작업 진행.".format(instance_selected, instance_needed))
            for i in range(folder_number): #folder_number = 2480으로 선언된 상태
                xml_name = location_win     +    image_Bbox    +   str(i+1).zfill(4)    + "/*.xml"
                img_dir = location_win + image_Bbox    +   str(i+1).zfill(4) + "/"
                label_dir = location_win + label_Bbox + str(i + 1).zfill(4) + "/"
                xml_list = glob.glob(xml_name)

                #image 찾아서 넣는 작업 진행.
                if len(xml_list) != 0:
                    find_Bbox(xml_list, instance_selected, img_dir, label_dir)

                instance_number_mid = Class_num[instance_selected]
                instance_needed_mid = Threshold - instance_number_mid

                if instance_needed_mid <= 0:
                    print("Bbox_{} 에서 Instance 채우기 완료. 다음 Iteration 진행.".format(str(i+1).zfill(4)))
                    break


#위 부분 너무 더러우니까 image 한개 입력으로 주면 Bounding_box 출력해주는 함수 만들면?
def normalization(center_x, center_y,width,height,img_width,img_height):

    center_x = round(center_x / img_width, 6)
    center_y = round(center_y / img_height, 6)
    width = round(width / img_width, 6)
    height = round(height / img_height, 6)

    return [center_x,center_y,width,height]

def find_Bbox(xml_list, instance_selected, img_dir, label_dir):
    tree = ET.parse(xml_list[0])  # xml_list[0] 에는 xml 주소가 적혀있음.
    root = tree.getroot()
    # print("주소 : ",xml_list[0])

    for image in root.findall('image'):
        # Image 이름 불러오기
        image_fullname = image.attrib['name']
        image_name, ext = os.path.splitext(image_fullname)
        # print("파일 이름 : ", image_name, ", ext : ",ext)


        if image_fullname not in used_img and os.path.isfile(img_dir + image_fullname):
            temp_box_attrib_for_img = []

            for box in image.findall('box'):
                temp_box_attrib_for_img.append(box.attrib['label'])
            #검사를 위해 이미지에 있는 모든 Bounding Box를 가져와서 배열에 저장함.

            if instance_selected in temp_box_attrib_for_img:

                used_img.append(image_fullname) #이미지 사용하기로 했으므로 append!

                for box in image.findall('box'):
                    Class_num[box.attrib['label']] += 1
                    ''' 선택된 instance가 이미지에 있는 경우에만 그 이미지를 선택하고 Bounding Box 값을 모두 업데이트 한 뒤에 이미지 옮기고 라벨 생성해주기.'''
                selected_img = img_dir + image_fullname # selected_img는 이미지 확장자까지 포함한 주소임
                selected_label = label_dir + image_name + '.txt' #image_name은 확장자 없는 이미지 이름, image_fullname은 확장자 있는 이미지 이름임.

                print(selected_img)
                print(selected_label)

                shutil.move(selected_img, new_location_win + "images/")
                shutil.move(selected_label, new_location_win + "labels/")



if __name__ == '__main__':
    Progress(ORDER, INSTANCE_THRESHOLD)
    print("사용된 이미지 : ", used_img)
    print("중복값이 존재하는지 : {}".format(False if len(set(used_img)) == len(used_img) else True))
    print("사용된 이미지 수 : ",len(used_img))
    print("Class num : ",Class_num)
    f_log =open(log_dir_win, 'w')

    f_log.write("------------------------DATA_EQUAL_SAMPLING_LOG------------------------\n")
    f_log.write("\n사용된 이미지 배열(옮긴 순서대로) : {}".format(used_img))
    f_log.write("\n중복값이 존재하는지 : {}".format(False if len(set(used_img)) == len(used_img) else True))
    f_log.write("\n사용된 이미지 수 : {}".format(len(used_img)))
    f_log.write("\nClass num : {}".format(Class_num))
    now = datetime.now()
    f_log.write("\n완료된 시간 : {}".format(now))
    f_log.close()


#테스트 해봄
#최초 경로에 있는(Test 폴더) 내용 : 파일 1,109, 폴더 8
#업데이트 후 기존 경로에 있는 (Test 폴더) 내용 : 파일 17, 폴더 8
#업데이트 후 새 경로에 있는(Test2 폴더) 내용 : 파일 1,092, 폴더 2
#Matches!