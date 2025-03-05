import math

def calculate_orders():
    # 첫 줄 입력: 참가자 수
    N = int(input().strip())
    
    # 둘째 줄 입력: 티셔츠 사이즈별 신청자 수
    sizes = list(map(int, input().strip().split()))
    
    # 셋째 줄 입력: 티셔츠 묶음 크기(T)와 펜 묶음 크기(P)
    T, P = map(int, input().strip().split())
    
    # 티셔츠 최소 주문 묶음 수 계산
    min_tshirt_bundles = sum(math.ceil(size / T) for size in sizes)
    
    # 펜 최대 주문 묶음 수 및 추가 펜 개수 계산
    max_pen_bundles = N // P
    extra_pens = N % P
    
    # 결과 출력
    print(min_tshirt_bundles)
    print(max_pen_bundles, extra_pens)

# 함수 실행
calculate_orders()