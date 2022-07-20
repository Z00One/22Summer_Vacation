import turtle
import random

# turtle 기본 설정
turtle.colormode(255)       # RGB 사용하기 위한 설정
t = turtle.Turtle()         # t라는 하나의 객체 생성
t.speed(0)                  # t의 속도 설정
t.screen.bgcolor("BLACK")   # 배경 색 설정

# 중간에 그리기 위해 위치 이동
t.penup()
t.goto(-200,0)
t.pendown()

# 그림 그리기
count = 0
while count < 400:
    # rgb값 난수로 정하기
    r           = random.randint(0,20)
    g           = random.randint(0,20)
    b           = random.randint(20,255)

    # 색 정하기
    t.color((r, g, b))

    # 펜굵기 정하기
    t.pensize(random.randint(0,5))

    # 그리기
    t.fd(400 - count)
    t.rt(200)

    count += 1

# 펜 치우기
t.hideturtle()

turtle.done()