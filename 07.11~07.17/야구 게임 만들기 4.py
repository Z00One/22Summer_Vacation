##### 중복되는 것들 함수 선언
def EndMsg(MsgValue0, MsgValue1) :
    print(MsgValue0 , MsgValue1 , "\n정답은", answer[0], answer[1], answer[2], "이에요")
    # 반복문 종료하기 위해 False return
    return False

########## 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
# random 호출
import random
# 필요한 변수들 선언
answer      =   []         # 답을 담아줄 변수

# 리스트에 3가지 값이 중복이 되지 않도록 출력
while len(answer) < 3 :
    value = random.randint(1,9)
    if value not in answer:
        answer.append(value)

########## 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력

# 필요한 변수 선언
try_count   =   1   # 횟수 카운트 변수
out_count   =   0   # 아웃 카운트 변수
flag        =   True

while flag:

    # 시도횟수 출력
    print("시도횟수 :",try_count)

    # 정수 3개 입력받기
    inputValue  =  [int(input("정수를 3개 입력하세요 \n")) for value in range(3)]

    # 필요한 변수들 만들기
    strike_count    =   0   # 스트라이크 카운트
    ball_count      =   0   # 볼 카운트
    
    ##### 입력 받은 값이 답과 맞는 지 판별하기
    for index in range(3):

        ## 스트라이크 -- 인덱스, 요소 두 개다 동일한 경우
        if inputValue[index] == answer[index]:
            strike_count += 1

        ## 볼        -- 요소만 동일한 경우
        elif inputValue[index] in answer:
            ball_count   += 1

    ## 아웃          -- 스트라이크, 볼 어느것도 없는 경우
    if strike_count == 0 and ball_count == 0:
        out_count += 1
    ##### 결과 값 출력하기
    print("Strike :", strike_count, "Ball :", ball_count, "Out :", out_count ,"\n")
    
    # 한 번 반복이 끝나면 시도횟수 카운트
    try_count += 1

    ##### 종료하는 경우

    # – Strike out == 2
    if out_count      >=2:
        flag = EndMsg("아웃횟수 초과","아까비 졌네용")  

    # - 3 Strike
    elif strike_count == 3:
        flag = EndMsg("정답 입니다","축하해요 이겼어요")

    # – 시도 횟수 >= 5
    elif try_count    >=5:
        flag = EndMsg("시도횟수 초과","아까비 졌네용")