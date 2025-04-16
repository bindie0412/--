# 상수 정의: 심폐내구력과 근력에 따른 스태미나 감소율
CARDIO_RATES = {
    'Good': 0.1,   # m당 감소율
    'Fair': 0.3,
    'Poor': 0.5
}

STRENGTH_RATES = {
    'Good': 1,     # kg·m당 감소율
    'Fair': 2,
    'Poor': 4
}

REFERENCE_TIME = 3600  # 기준 시간(1시간 = 3600초)

# 사용자 입력
cardio = input("심폐내구력 수준을 입력하세요 (Good/Fair/Poor): ").capitalize()
strength = input("근력 수준을 입력하세요 (Good/Fair/Poor): ").capitalize()
backpack_weight = float(input("배낭 무게(kg)를 입력하세요: "))

# 예시 경로 (거리: m, 고도: m)
ROUTES = {
    'A': {'거리': 1000, '고도': 60},
    'B': {'거리': 1200, '고도': 30},
    'C': {'거리': 800, '고도': 90}
}

# 보폭 및 보행 속도(고정)
STRIDE_LENGTH = 1    # 1m/보
TIME_PER_STRIDE = 1  # 1초/보

print("\n=== 경로 분석 결과 ===")

for route_name, route in ROUTES.items():
    distance = route['거리']
    elevation = route['고도']
    
    # 이동 시간 계산 (초)
    move_time = (distance / STRIDE_LENGTH) * TIME_PER_STRIDE
    
    # 스태미나 감소 계산
    cardio_rate = CARDIO_RATES[cardio]
    strength_rate = STRENGTH_RATES[strength]
    
    # 고도 스태미나 감소
    elevation_loss = (elevation * cardio_rate * move_time) / REFERENCE_TIME
    
    # 거리/배낭 스태미나 감소
    distance_loss = (distance * backpack_weight * strength_rate * move_time) / REFERENCE_TIME
    
    total_loss = elevation_loss + distance_loss
    remaining_stamina = 100 - total_loss
    
    # 결과 판단
    if remaining_stamina >= 0:
        result = f"완주 가능! 남은 스태미나: {remaining_stamina:.1f}"
    else:
        needed = abs(remaining_stamina)
        result = f"완주 불가. {needed:.1f} 스태미나 추가 필요"
    
    # 출력
    print(f"\n경로 {route_name}:")
    print(f"거리: {distance}m | 고도: {elevation}m")
    print(f"고도 스태미나 감소: {elevation_loss:.1f}")
    print(f"거리/배낭 스태미나 감소: {distance_loss:.1f}")
    print(f"총 스태미나 소모: {total_loss:.1f}")
    print(f"결과: {result}")