def recursion():
    keyName = "강주원"
    name = input("사용자 이름을 입력하세요.")

    if name == keyName:         # 값이 맞으면 value 리턴
        return "value"

    else:
        print("다시", end=" ")  # 값이 다르면 함수 recursion 리턴 --> 맞는 값이 나올 때까지 반복된다.
        return recursion()

print(recursion())