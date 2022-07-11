# [2, 4, 6]
# [1, 4, 2] -->1Strike 1Ball
# 시도 횟수 5회 이상, strike out == 2 인경우 게임 짐
import random
# 0~9사이의 정수 난수로 생성
answer = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]
# 시도 횟수
try_count = 0
out_count = 0
while True:
    try_count += 1
    strike_count = 0
    ball_count = 0
    print("시도횟수:", try_count)
    # 정수 3개 입력받기
    inputValue = input("정수 3개를 입력하세용~~^__^ \n")
    inputValue = [int(inputValue[0]),int(inputValue[2]),int(inputValue[4])]
    # 답이랑 비교하기
    for value in range(len(answer)):
        for compare_value in range(len(inputValue)):
            # strike
            if value == compare_value and answer[value] == inputValue[compare_value]:
                strike_count+=1
            # ball
            if value != compare_value and answer[value] == inputValue[compare_value]:
                ball_count += 1
    print()
    if strike_count >= 1:
        print(strike_count,"Strike",end=" ")
    if ball_count >= 1:
        print(ball_count, "Ball", end=" ")
    if strike_count == 0 and ball_count == 0:
        out_count +=1
        print("Out : 아웃 %d번"%out_count, end=" ")
    print()
    print()
    # 진 경우
    if out_count>=2 or try_count>=5:
        print("게임횟수 초과")
        print("아까비~~~~졌네용..")
        print("정답은:",answer[0],answer[1],answer[2],"입니다.")
        print("계속하려면 아무 키나 누르십시오 . . .")
        break

        