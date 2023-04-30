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


from PIL import Image
from PIL import ImageDraw
import numpy as np
import matplotlib.pyplot as plt

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

for i in range(10):
    for j in range(10):
        print("{} {}".format(i,j))
