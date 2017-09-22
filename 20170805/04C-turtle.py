# 반복 기능으로 도형을 그리는 프로그램
import turtle as t

# 삼각형 그리기
for x in range(3):       # 세 번 반복합니다.
    t.forward(100)       # 거북이 100만큼 앞으로 이동합니다.
    t.left(120)          # 거북이 왼쪽으로 120도 회전합니다.

# 사각형 그리기
for x in range(4):       # 네 번 반복합니다.
    t.forward(100)       # 거북이 100만큼 앞으로 이동합니다.
    t.left(90)           # 거북이 왼쪽으로 90도 회전합니다.

# 원 그리기
t.circle(50)             # 반지름이 50인 원을 그립니다.
