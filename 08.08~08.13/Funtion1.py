# call-by-value
def foo(argA):
    argA = argA + 2

value = 1

foo(value)      # value에 저장된 값을 복사하여 사용함
                # Primitive variables -> int, float, string, boolean

# call-by-reference
def bar(a):
    a.append(1)

value = [1, 2]  # value의 메모리 주소를 가져와서 사용함
                # Reference variables -> Object -> List, Tuple, Dictionary

###########################################

# positional argument
def foo (a, b, c):
    print(a, b, c)

foo(1, 2, 3)

# keyword argument
def bar (a, b, c):
    print(a, b, c)

bar(b=2, a=1, c=3)

# default argument -> 매개변수에 초기값 설정, 인자가 없어도 오류 발생 안 함 -> [n : ] 범위만 사용가능
def han (a, b=2, c=3):
    print(a, b, c)

han(1)

# arbitrary positional arguments -> 인자값이 tuple로 전달이 된다.
def pos(*a):
    print(type(a))
    for value in a:
        print(value)

pos(1, 2, 3)

# arbitrary keyword argument
def fox(**dict):
    print(type(dict))
    for key, value in dict.items():
        print(key, value)

fox(name = "juwon", gender = "male")