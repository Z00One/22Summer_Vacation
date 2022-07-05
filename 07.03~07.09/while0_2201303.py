# 값 입력 받기 --> 형 변환 --> int()
num = int(input("양의 정수를 입력하세요"))

# 출력 횟수를 카운트 해줄 변수
range_num = 1

# 얼마나 출력 할 지 정하는 루프
while range_num <= num:

    # 반복이 돌면 num_count 값 리셋
    num_count = 1

    # 출력하는 루프 
    while num_count <= range_num:

        # 1에서 1까지 1에서 2 까지 ... 1에서 num까지 출력
        print(num_count, end='')

        # 반복이 끝나면 카운트
        num_count += 1

    # 반복이 끝나면 출력횟수 카운트
    range_num += 1
    
    # 한 번 출력하면 줄 바꾸기
    print()
