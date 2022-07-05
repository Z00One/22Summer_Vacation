# 값 입력받기 --> 형 변환 필요 --> int()
num = int(input("양의 정수를 입력하세요"))

# 입력 받은 값 만큼 반복
for num_value in range(1,num+1):

    # 입력 받은 값이 나올 때까지 반복 1 -> 12 -> 123 ,,, -> 123...n
    for input_num in range(num_value):
        print(input_num + 1, end='')

    # 단 바꿔주기
    print()