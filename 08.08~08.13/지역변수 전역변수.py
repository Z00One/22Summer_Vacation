def bar():
    print(value)

def han():
    value = 2
    bar()

def   foo():
    value = 1
    han()

value = 3

foo()     # 3 -> 전역 변수는 main에 선언된 것 나머지 공간에 선언된 것인 지역변수
          #   -> 해당 공간의 변수(지역 변수)가 없으면 전역변수에서 찾는다.