
########## 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
# random 호출
import random
# 필요한 변수들 선언
answer           =   []         # 답을 담아줄 변수
Range_List       =   [0] * 3    # for 문의 range를 조절할 변수

# 리스트에 3가지 값이 중복이 되지 않도록 출력
# for 문의 range 의 길이가 계속 길어지도록
for answer_index in Range_List:  # list 자리에 range 함수를 쓸 때 range(value) 의 value 값은 처음 값대로만 적용된다. --> list를 사용한다.
    randomValue = random.randint(1,9)
    # 만약 난수가 리스트에 있을 시에 Range_List 값을 올려주고 한 번 더 하고 컨티뉴
    if randomValue in answer:
        Range_List.append("0")
        continue
    answer.append(randomValue)


########## 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력

# 필요한 변수 선언
try_count       =   1   # 횟수 카운트 변수
out_count       =   0   # 아웃 카운트 변수

while True:
    # 시도횟수 출력
    print("시도횟수 :",try_count)
    # 정수 3개 입력받기
    inputValue  =   [int(input("정수를 3개 입력하세요 \n")) for value in range(3)]

    # 필요한 변수들 만들기
    strike_count    =   0   # 스트라이크 카운트
    ball_count      =   0   # 볼 카운트
    index_value     =   0   # 인덱스 카운트
    
    ##### 입력 받은 값이 답과 맞는 지 판별하기
    for value in inputValue:
        # 입력 받은 값이 답 안에 있는 경우
        if value in answer:
        # 인덱스 값이 같다면 스트라이크
            if value == answer[index_value]:
                strike_count    += 1
            # 아니면 볼
            else:
                ball_count      += 1
        index_value  += 1

    ##### 결과 값 출력하기
    print()
    # 스트라이크 부터 출력 하기
    if strike_count:
        print(strike_count,"Strike",end=' ')
    # 볼 출력
    if ball_count:
        print(ball_count,"Ball",end=' ')
    # 아웃출력 -- 하나도 안 맞는 경우
    if not(strike_count) and not(ball_count):
        out_count += 1
        print(out_count,"아웃",end=" ")
    print()
    print()

    # 한 번 반복이 끝나면 시도횟수 카운트

    try_count += 1

    ##### 종료하는 경우
    if  try_count>=5   or   out_count>=2   or  strike_count == 3 :
        # 종료 안내문 출력
        # – 시도 횟수 >= 5
        if try_count>=5:
            print("시도횟수 초과")
            print("아까비 졌네용")
        # – Strike out == 2
        elif out_count>=2:
            print("아웃횟수 초과")
            print("아까비 졌네용")
        # - 3 Strike
        else:
            print("이겼네요")
        print("정답은",answer[0], answer[1], answer[2], "이에요")
        break
