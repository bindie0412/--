stamina = 100.0 # 초기 스태미나
reference_time = 3600 # 기준 시간(1시간 = 3600초)
simpe = { #심폐지구력 수준
    'Good' : 0.1,
    'Fair' : 0.3,
    'Poor' : 0.5
}

strength = { # 근력 수준
    'Good' : 0.01,
    'Fair' : 0.02,
    'Poor' : 0.04
}

reference_time = 3600

simper = input("심폐내구력 수준을 입력하세요 (Good/Fair/Poor): ")
strengths = input("근력 수준을 입력하세요 (Good/Fair/Poor): ")
weight = float(input("배낭 무게(kg)를 입력하세요: "))
bopoc = int(input("보폭을 입력하세요(m): "))
socdo = int(input("보행 속도를 입력하세요(초): "))

A_route = {'거리': 1000, '고도': 60}#수정 필요
B_route = {'거리': 1200, '고도': 30}#수정 필요
C_route = {'거리': 800, '고도': 90}#수정 필요

def calculate_stamina(route):
    global stamina# '스태미나' 변수를 전역으로 사용, 왜쓰는진 모르는데 이거 있어야 실행됨....
    distance = route['거리']
    elevation = route['고도']
    sigan = (distance / bopoc) * socdo# 이동 시간 계산 (초)
    simpe_rate = simpe[simper]# 심폐내구력 감소율
    strength_rate = strength[strengths]# 근력 감소율
    elevation_loss = (elevation * simpe_rate * sigan) / reference_time# 고도 스태미나 감소
    distance_loss = (distance * weight * strength_rate * sigan) / reference_time# 거리/배낭 스태미나 감소
    total_loss = elevation_loss + distance_loss# 총 스태미나 감소
    stamina -= total_loss# 남은 스태미나 계산
    return stamina

calculate_stamina(A_route)
print("A 경로 남은 스태미나:" ,(stamina))
calculate_stamina(B_route)
print("B 경로 남은 스태미나:" ,(stamina))
calculate_stamina(C_route)
print("C 경로 남은 스태미나:" ,(stamina))