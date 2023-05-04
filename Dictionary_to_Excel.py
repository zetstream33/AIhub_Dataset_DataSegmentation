import pandas as pd
import openpyxl

Class_num = {'bicycle': 52688, 'bus': 48081, 'car': 790797, 'carrier': 9795, 'cat': 164, 'dog': 9912, 'motorcycle': 59326, 'movable_signage': 132077, 'person': 427416, 'scooter': 1983, 'stroller': 6059, 'truck': 140315, 'wheelchair': 3819, 'barricade': 17901, 'bench': 24340, 'bollard': 293352, 'chair': 29831, 'fire_hydrant': 11532, 'kiosk': 9529, 'parking_meter': 328, 'pole': 400846, 'potted_plant': 72470, 'power_controller': 8094, 'stop': 17889, 'table': 9057, 'traffic_light': 155814, 'traffic_light_controller': 8287, 'traffic_sign': 185597, 'tree_trunk': 439764}

# 딕셔너리를 DataFrame으로 변환
df = pd.DataFrame(list(Class_num.items()), columns=['Class', 'Count'])

# DataFrame을 엑셀 파일로 저장
df.to_excel('class_counts.xlsx', index=False, engine='openpyxl')
