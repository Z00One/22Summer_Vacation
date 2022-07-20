# 요구사항을 만족하는 집 그리기

import turtle as t

t.shape("turtle")

name        = input("이름을 입력하세요.  ")
size        = int(input("집의 크기 몇 평으로 할까요? 정수를 입력하세요  "))
house_color = input("집의 색은 무엇으로 할까요? 영어로 입력하세요  ")
window      = input("창문을 낼까요? yes or no  ")

#집색깔
t.color(house_color)

#몸체 그리기
for i in range(4) :
    t.fd(size)
    t.right(90)

#지붕 그리기
for i in range(3) :
    t.fd(size)
    t.lt(120)

if window == "yes" :
    #창문틀 그리기
    t.up()
    t.goto(size/4,-size/4)
    t.down()

    for i in range(4) :
        t.fd(size/2)
        t.right(90)

#창문자세히(가로선,세로선)
    t.up()
    t.goto(size/2,-size/4)
    t.down()
    t.right(90)
    t.fd(size/2)

    t.up()
    t.goto(size/4,-size/2)
    t.down()
    t.lt(90)
    t.fd(size/2)

#칭찬하기
print("\t"+name+"씨 참 잘그렸어요!")
t.write("\t"+name+"씨 참 잘그렸어요!")
t.done()