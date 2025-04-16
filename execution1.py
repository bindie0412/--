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
    global stamina
    distance = route['거리']
    elevation = route['고도']
    sigan = (distance / bopoc) * socdo
    simpe_rate = simpe[simper]
    strength_rate = strength[strengths]
    elevation_loss = (elevation * simpe_rate * sigan) / reference_time
    distance_loss = (distance * weight * strength_rate * sigan) / reference_time
    total_loss = elevation_loss + distance_loss
    stamina -= total_loss
    return stamina

calculate_stamina(A_route)
print("A 경로 남은 스태미나:" ,(stamina))
calculate_stamina(B_route)
print("B 경로 남은 스태미나:" ,(stamina))
calculate_stamina(C_route)
print("C 경로 남은 스태미나:" ,(stamina))