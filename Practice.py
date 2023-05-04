# def normalization(center_x, center_y,width,height,img_width,img_height):
#
#     center_x = round(center_x / img_width, 6)
#     center_y = round(center_y / img_height, 6)
#     width = round(width / img_width, 6)
#     height = round(height / img_height, 6)
#
#     return [center_x,center_y,width,height]
#
# x, y, w, h = normalization(960,540,192,108,1920,1080)
#
# print("{} {} {} {}".format(x,y,w,h))  -> Normalization 함수 정상 작동 확인 (2023.03.24 00:25)




    # def pil_draw_rect(image, point1, point2):
    #     draw = ImageDraw.Draw(image)
    #     draw.rectangle((point1, point2), outline=(0, 0, 255), width=3)
    #
    #     return image
    #
    # def pil_draw_point(image, point):
    #     x, y = point
    #     draw = ImageDraw.Draw(image)
    #     radius = 2
    #     draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(0, 255, 0))
    #
    #     return image
    #
    #
    # image = Image.open("C:/Users/dldjw/OneDrive/바탕 화면/Dev/XML_TO_YOLO_PROJECT/My_data/Test/Bbox_0001/MP_SEL_000001.jpg")
    # image = pil_draw_rect(image, (1272.39, 451.90), (1331.40, 670.79))
    # image = pil_draw_point(image, (1272.39, 451.90))
    # # image = pil_draw_point(image, (1331.40, 670.79))
    #
    #
    # plt.imshow(np.array(image))
    #
    # image.show()

#여기서 알 수 있는 것 ->

import os
# import glob
# empty_list = []
#
# for i in range(2480):
#     # xml_name = "C:/Users/dldjw/OneDrive/바탕 화면/Test/images/"  # -> 여기 뒤에 Bbox_n 폴더와 xml 파일 찾아서 붙여넣어 파일 이름 완성하면 됨
#     # xml_name += "Bbox_"+str(i+1).zfill(4)
#     # print(xml_name)
#
#     target = "H:\내 드라이브\Capstone1\Dataset_zip_original\Bbox_{}\*.xml".format(str(i+1).zfill(4))
#     xml_list = glob.glob(target)
#     print("폴더 : Bbox_{}".format(str(i+1).zfill(4)),xml_list)
#     # if len(xml_list) == 0 : empty_list.append(str(i+1).zfill(4))
#     if len(xml_list) != 0:
#
#     else:
#         empty_list.append(str(i + 1).zfill(4))

# for i in range(10):
#     for j in range(10):
#         print("{} {}".format(i,j))

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

for name in enumerate(Class_index):
    # print(name)
    Class_num[name[1]] = 0

Class_num['motorcycle'] += 1
Class_num['bus'] += 3
Class_num['bus'] += 3

print(Class_num)
print(Class_index['motorcycle'])


