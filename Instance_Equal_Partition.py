import xml.etree.ElementTree as ET
import glob
import numpy as np
#
# folder_name = ['train']
# Class_index = {'bicycle' : 0
#     ,'bus':1
#     ,'car':2
#     ,'carrier':3
#     ,'cat':4
#     ,'dog':5
#     ,'motorcycle':6
#     ,'movable_signage':7
#     ,'person':8
#     ,'scooter':9
#     ,'stroller':10
#     ,'truck':11
#     ,'wheelchair':12
#     ,'barricade':13
#     ,'bench':14
#     ,'bollard':15
#     ,'chair':16
#     ,'fire_hydrant':17
#     ,'kiosk':18
#     ,'parking_meter':19
#     ,'pole':20
#     ,'potted_plant':21
#     ,'power_controller':22
#     ,'stop':23
#     ,'table':24
#     ,'traffic_light':25
#     ,'traffic_light_controller':26
#     ,'traffic_sign':27
#     ,'tree_trunk':28} #Class Annotation을 위한 {클래스 이름 : 라벨 넘버} 1:1 대응 Dictionary
# Class_num = {} #Instance 개수를 구하기 위한 {인스턴스(클래스) 이름 : 인스턴스(클래스) 갯수} 1:1 대응 Dictionary
#
# for name in enumerate(Class_index):
#     # print(name)
#     Class_num[name[1]] = 0
#
# empty_list = []
# exist_list = []
#
# folder_number = 2480
# for f_name in folder_name:
#     for i in range(folder_number):
#         xml_name = "/home/zetstream/Dataset/" + f_name + "/images/" + "Bbox_"+str(i+1).zfill(4) + "/"
#         # -> 여기 뒤에 Bbox_n 폴더와 xml 파일 찾아서 붙여넣어 파일 이름 완성하면 됨
#
#         # target = "H:\내 드라이브\Capstone1/train\images\Bbox_{}\*.xml".format(str(i + 1).zfill(4))
#         target = xml_name + "*.xml"
#         xml_list = glob.glob(target)
#
#         print("폴더 : Bbox_{}".format(str(i + 1).zfill(4)), xml_list)
#         # if len(xml_list) == 0 : empty_list.append(str(i+1).zfill(4))
#         if len(xml_list) != 0:
#             tree = ET.parse(xml_list[0]) #xml_list[0] 에는 xml 주소가 적혀있음.
#             root = tree.getroot()
#
#             for image in root.findall('image'):
#                 #Image 이름 불러오기
#                 image_fullname = image.attrib['name']
#                 for box in image.findall('box'): # 라벨 내용 한줄 한줄 작성하는 코드
#
#                     print("instance detected : ", box.attrib['label'])  #-> box.attrib는 dictionary 타입이므로 이런 식으로 접근 가능!
#                     Class_num[box.attrib['label']] += 1
#
#         else:
#             empty_list.append("Bbox_{}".format(str(i + 1).zfill(4)))
#         # print(*exist_list, sep=',')
#
# print(Class_num)

# RESULT
# {'bicycle': 52688, 'bus': 48081, 'car': 790797, 'carrier': 9795, 'cat': 164, 'dog': 9912, 'motorcycle': 59326, 'movable_signage': 132077, 'person': 427416, 'scooter': 1983, 'stroller': 6059, 'truck': 140315, 'wheelchair': 3819, 'barricade': 17901, 'bench': 24340, 'bollard': 293352, 'chair': 29831, 'fire_hydrant': 11532, 'kiosk': 9529, 'parking_meter': 328, 'pole': 400846, 'potted_plant': 72470, 'power_controller': 8094, 'stop': 17889, 'table': 9057, 'traffic_light': 155814, 'traffic_light_controller': 8287, 'traffic_sign': 185597, 'tree_trunk': 439764}




'''def calculate_class_weights(class_counts):
    total_count = sum(class_counts.values())
    class_weights = {key: total_count / (len(class_counts) * count) for key, count in class_counts.items()}
    normalized_weights = np.array(list(class_weights.values()))
    normalized_weights = normalized_weights / np.sum(normalized_weights)
    return normalized_weights

class_counts = {'bicycle': 52688, 'bus': 48081, 'car': 790797, 'carrier': 9795, 'cat': 164, 'dog': 9912, 'motorcycle': 59326, 'movable_signage': 132077, 'person': 427416, 'scooter': 1983, 'stroller': 6059, 'truck': 140315, 'wheelchair': 3819, 'barricade': 17901, 'bench': 24340, 'bollard': 293352, 'chair': 29831, 'fire_hydrant': 11532, 'kiosk': 9529, 'parking_meter': 328, 'pole': 400846, 'potted_plant': 72470, 'power_controller': 8094, 'stop': 17889, 'table': 9057, 'traffic_light': 155814, 'traffic_light_controller': 8287, 'traffic_sign': 185597, 'tree_trunk': 439764}

class_weights = calculate_class_weights(class_counts)
print(class_weights) '''
#Result

# [1.70651511e-03 1.87002908e-03 1.13699051e-04 9.17946588e-03
#  5.48249197e-01 9.07111262e-03 1.51557274e-03 6.80760983e-04
#  2.10363834e-04 4.53418398e-02 1.48395558e-02 6.40792989e-04
#  2.35435633e-02 5.02278467e-03 3.69403732e-03 3.06501637e-04
#  3.01407490e-03 7.79681480e-03 9.43570871e-03 2.74124598e-01
#  2.24307760e-04 1.24069088e-03 1.11085827e-02 5.02615397e-03
#  9.92744488e-03 5.77052565e-04 1.08498695e-02 4.84452164e-04
#  2.04457091e-04]

'''
앞서 작성한 `calculate_class_weights` 함수를 사용하여 클래스 가중치를 계산한 후, `train.yaml` 파일에 클래스 가중치를 포함하도록 수정할 수 있습니다.
이렇게 계산된 클래스 가중치를 출력한 후, 이 값을 `train.yaml` 파일에 추가합니다.

yaml
# train.yaml
nc: 27  # number of classes
names: ['bicycle', 'bus', 'car', 'carrier', 'cat', 'dog', 'motorcycle', 'movable_signage', 'person', 'scooter', 'stroller', 'truck', 'wheelchair', 'barricade', 'bench', 'bollard', 'chair', 'fire_hydrant', 'kiosk', 'parking_meter', 'pole', 'potted_plant', 'power_controller', 'stop', 'table', 'traffic_light', 'traffic_light_controller', 'traffic_sign', 'tree_trunk']
class_weights: [0.03278483, 0.03597123, 0.00218252, 0.17634487, 1.05139186, 0.17390645, 0.02908334, 0.01306729, 0.00404326, 0.8698652, 0.28460669, 0.01230413, 0.45250018, 0.09650609, 0.07111326, 0.00588237, 0.05792409, 0.14971037, 0.18166813, 5.25924581, 0.00431313, 0.02385377, 0.21412846, 0.09598396, 0.19157151, 0.01107158, 0.02089808, 0.03737279, 0.00393271]
```
이제 데이터 증강 및 클래스 가중치가 설정되었습니다. YOLOv5를 사용하여 훈련을 시작할 준비가 되었습니다.
훈련을 시작하기 전에, `train.py`를 실행할 때 클래스 가중치를 사용하도록 옵션을 추가해야 합니다. `train.py`의 명령행 인수에 `--class_weights`를 추가하십시오.

(bash 터미널에서)
python train.py --img 640 --batch 16 --epochs 50 --data train.yaml --cfg yolov5s.yaml --weights yolov5s.pt --class_weights
이제 훈련이 시작되며, 데이터 불균형 문제를 완화하기 위해 데이터 증강 및 클래스 가중치가 사용됩니다.'''



'''위 코드는 전체 폴더에서 Instance 분포를 나타내지 않고 갯수를 세는 코드. 각 인스턴스가 총 몇개씩 존재하는지 전체 이미지에서 찾아냄
아래 코드 부터 전체 폴더에서 Instance 분포를 나타내도록 함. 위 코드에서 사전에 계산된 전체 Instance 각각의 개수를 재분배 하여 균등한 Train Set 제작함.'''



Order = ['scooter','wheelchair','stroller','power_controller','traffic_light_controller','table','kiosk','carrier','dog','fire_hydrant','stop','barricade','bench','chair','bus','bicycle','motorcycle','potted_plant','movable_signage','truck','traffic_light','traffic_sign','bollard','pole','person','tree_trunk','car']
