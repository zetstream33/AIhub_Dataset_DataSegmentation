'''LIST VARIABLE'''
ORDER = ['scooter','wheelchair','stroller','power_controller','traffic_light_controller','table','kiosk','carrier','dog','fire_hydrant','stop','barricade','bench','chair','bus','bicycle','motorcycle','potted_plant','movable_signage','truck','traffic_light','traffic_sign','bollard','pole','person','tree_trunk','car']
used_img = []

'''INT VARIABLE'''
INSTANCE_THRESHOLD = 1700

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
#                                            Class_num의 해당되는 int 값들은 전부 0으로 설정되어 있는 상태.


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



def Progress(order, threshold):
    for instance_selected in range(order):


if __name__ == '__main__':
    Progress(ORDER, INSTANCE_THRESHOLD)