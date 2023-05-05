import xml.etree.ElementTree as ET
import os

def normalization(center_x, center_y,width,height,img_width,img_height):

    center_x = round(center_x / img_width, 6)
    center_y = round(center_y / img_height, 6)
    width = round(width / img_width, 6)
    height = round(height / img_height, 6)

    return [center_x,center_y,width,height]


folder_number = 2480 #폴더 갯수, 2480개지만 안전을 위해 저장하고 보관할떈 0으로 적음

for i in range(folder_number):
    # xml_name = "C:/Users/dldjw/OneDrive/바탕 화면/Test/images/"  # -> 여기 뒤에 Bbox_n 폴더와 xml 파일 찾아서 붙여넣어 파일 이름 완성하면 됨
    # xml_name += "Bbox_"+str(i+1).zfill(4)
    # print(xml_name)

    target = "H:\내 드라이브\Capstone1/train\images\Bbox_{}\*.xml".format(str(i + 1).zfill(4))
    xml_list = glob.glob(target)
    print("폴더 : Bbox_{}".format(str(i + 1).zfill(4)), xml_list)
    # if len(xml_list) == 0 : empty_list.append(str(i+1).zfill(4))
    if len(xml_list) != 0:
        tree = ET.parse(xml_list[0]) #xml_list[0] 에는 xml 주소가 적혀있음.
        root = tree.getroot()
        # folder = "H:/내 드라이브/Capstone1/labels/Bbox_{}".format(str(i+1).zfill(4))
        # os.mkdir(folder) 무조건 주석 처리 할 것!!!!!!!!!!!!!!! 폴더 생성하는 코드
        # time.sleep(1)
        exist_list.append("train/images/Bbox_{}".format(str(i + 1).zfill(4)))
        for image in root.findall('image'):
            #Image 이름 불러오기
            image_fullname = image.attrib['name']
            image_name, ext = os.path.splitext(image_fullname)
            print("파일 이름 : ", image.attrib['name'])

            # Image size 정보(기본 1920*1080) 이지만 Just in case
            image_width = int(image.attrib['width']) #      1920(픽셀)
            image_height = int(image.attrib['height']) #    1080(픽셀)

            #label 위치할 주소 받아오기
            label_context=""

            for box in image.findall('box'): # 라벨 내용 한줄 한줄 작성하는 코드

                # print("label name : ", box.attrib['label'])  #-> box.attrib는 dictionary 타입이므로 이런 식으로 접근 가능!

                # text = str(Class_index[box.attrib['label']]) +" " + box.attrib['xtl']+" " + box.attrib['ytl']+" " + box.attrib['xbr']+" " + box.attrib['ybr']
                # print("XML Format : ",text)

               ''' center_x = round((float(box.attrib['xtl']) + float(box.attrib['xbr'])) / 2 , 6)
                center_y = round((float(box.attrib['ytl']) + float(box.attrib['ybr'])) / 2 , 6)
                width = round((float(box.attrib['xbr']) - float(box.attrib['xtl']))  , 6)
                height = round((float(box.attrib['ybr']) - float(box.attrib['ytl']))  , 6)

                center_x, center_y, width, height = normalization(center_x,center_y,width,height,image_width,image_height)
                # print("{} {} {} {} {}".format(str(Class_index[box.attrib['label']]), center_x,center_y,width,height))         # print("YOLO Format : {} {} {} {} {}".format(str(Class_index[box.attrib['label']]), center_x,center_y,width,height))
                label_context += "{} {} {} {} {}\n".format(str(Class_index[box.attrib['label']]), center_x,center_y,width,height)

            print("label : {}\n{}".format(image_name.rstrip('jpg')+'.txt',label_context))
            label_name = "{}.txt".format(image_name)
            label_location = "H:/내 드라이브/Capstone1/labels/Bbox_{}/{}".format(str(i + 1).zfill(4),label_name)
            file = open(label_location,'w')
            file.write(label_context)
            file.close()'''
    else:
        empty_list.append("Bbox_{}".format(str(i + 1).zfill(4)))


print(*exist_list, sep=',')

