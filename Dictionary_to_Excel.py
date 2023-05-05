import pandas as pd
import openpyxl

Class_num = {'bicycle': 52688, 'bus': 48081, 'car': 790797, 'carrier': 9795, 'cat': 164, 'dog': 9912, 'motorcycle': 59326, 'movable_signage': 132077, 'person': 427416, 'scooter': 1983, 'stroller': 6059, 'truck': 140315, 'wheelchair': 3819, 'barricade': 17901, 'bench': 24340, 'bollard': 293352, 'chair': 29831, 'fire_hydrant': 11532, 'kiosk': 9529, 'parking_meter': 328, 'pole': 400846, 'potted_plant': 72470, 'power_controller': 8094, 'stop': 17889, 'table': 9057, 'traffic_light': 155814, 'traffic_light_controller': 8287, 'traffic_sign': 185597, 'tree_trunk': 439764}
Class_num_Equal_result = {'bicycle': 3592, 'bus': 2528, 'car': 35282, 'carrier': 1774, 'cat': 5, 'dog': 1947, 'motorcycle': 3216, 'movable_signage': 7838, 'person': 32754, 'scooter': 121, 'stroller': 1842, 'truck': 5882, 'wheelchair': 1817, 'barricade': 1703, 'bench': 1713, 'bollard': 15419, 'chair': 3119, 'fire_hydrant': 1705, 'kiosk': 1739, 'parking_meter': 29, 'pole': 18460, 'potted_plant': 4021, 'power_controller': 1749, 'stop': 1711, 'table': 1799, 'traffic_light': 8700, 'traffic_light_controller': 1752, 'traffic_sign': 8376, 'tree_trunk': 19083}
# 딕셔너리를 DataFrame으로 변환
df = pd.DataFrame(list(Class_num_Equal_result.items()), columns=['Class', 'Count'])

# DataFrame을 엑셀 파일로 저장
df.to_excel('class_counts_equal_result.xlsx', index=False, engine='openpyxl')
