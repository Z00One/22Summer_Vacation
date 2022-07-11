import random
# 난수 3개 중복되지 않게 만들기 --> list
answer = []

# 난수를 담는 list의 요소의 갯수는 3개
while len(answer)<3:
    value = random.randint(0,9)
    if value not in answer:
        answer.append(value)


out_count   = 0
try_count   = 0
flag        = True
while flag:
    try_count       +=  1
    strike_count    =   0
    ball_count      =   0

    # 값 3개 입력받기
    print("시도횟수:",try_count)
    inputValue = input("정수 3개를 입력하세용~~^__^ \n")
    inputValue = [int(inputValue[0]), int(inputValue[1]), int(inputValue[2])]

    # 값 비교하기
    for compareValue in range(len(inputValue)):
        # 입력값이 안에 있을 때
        if inputValue[compareValue] in answer:
            # 순서가 맞다면 스트라이크
            if inputValue[compareValue] == answer[compareValue]:
                strike_count += 1
            # 아니면 볼
            else : 
                ball_count += 1
    print()
    
    # 결과 출력하기
    if strike_count >= 1:
        print(strike_count,"Strike", end=" ")
    if ball_count >= 1:
        print(ball_count, "Ball", end=" ")
    # 입력값이 답과 모두 다를 때 아웃
    if strike_count == 0 and ball_count == 0:
        out_count+=1
        print("Out: 아웃 %d번"%out_count, end=" ")
    print()
    
    # 시도 횟수가 5가 넘으면 종료
    if try_count >= 5:
        flag = False
        print("게임횟수 초과")
        print("아까비~~~~졌네용..")
        print("정답은:",answer[0],answer[1],answer[2],"입니다.")
        restart = input("계속하려면 아무 키나 누르십시오...")
        if len(restart) >= 0:
            flag = True
        
    if out_count>2:
        flag = False
        print("아웃 횟수 초과")
        print("아까비~~~~졌네용..")
        print("정답은:",answer[0],answer[1],answer[2],"입니다.")
        restart = input("계속하려면 아무 키나 누르십시오...")
        if len(restart) >= 0:
            flag = True
    # 이긴 경우
    if strike_count == 3:
        flag = False
        print("축하해요 이겼어요")
        print("정답은:",answer[0],answer[1],answer[2],"입니다.")
        restart = input("계속하려면 아무 키나 누르십시오...")
        if len(restart) >= 0:
            flag = True
