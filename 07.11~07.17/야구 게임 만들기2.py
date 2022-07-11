# 모듈 import
import random
# 정답 값을 담을 리스트 만들어 주기
answer_list     =    []
# 요소가 중복되지 않는, 1에서 9까지의 범위로 난수 만들어주기
# 정답 리스트에는 원소가 3가지
while len(answer_list) < 3 :
    answerValue       =    random.randint(1,9)
    # 정답 리스트 안에 값이 없는 경우만 넣어 주기
    if answerValue not in answer_list:
        answer_list.append(str(answerValue))


# 게임 안에서 계속 유지되어야 하는 변수 선언

# 시도 횟수 카운트할 변수 선언
try_count       =   0   
# 아웃 카운트할 변수 선언
out_count       =   0
# 게임을 On/Off 해 줄 변수 선언
flag            =   True


# 게임 돌리기
while flag:
   
# 게임 안에서 계속 초기화 해줘야하는 변수 선언
        
    # 시도횟수 카운트
    try_count   +=  1
    # Strike 카운트 해줄 변수 선언
    Strike_count =  0
    # Ball 카운트 해줄 변수 선언
    Ball_count   =  0

    
    # 시도횟수 출력 하기
    print("시도횟수 :", try_count)
    
    
    # 값을 입력받기
    inputValue          = input("정수 세 개를 입력하세요.")
    # 입력 받은 값의 리스트 만들어 주기
    inputValue_list     = [inputValue[0], inputValue[1], inputValue[2]]


    # 입력 받은 값을 정답과 비교해주기
    for compareValue in range(len(inputValue_list)):
        # 요소값이 정답 리스트에 있는 지 확인
        if inputValue_list[compareValue] in answer_list:
            # 인덱스 값도 맞다면 Strike
            if inputValue_list[compareValue] == answer_list[compareValue]:
                Strike_count    +=  1
            # 인덱스 값이 다르면 Ball
            else :
                Ball_count      +=  1


    # 값을 출력하기

        # 공백 출력
        print()

        # Strike값 Ball값 출력해주기
        if Strike_count:
            print(Strike_count,"Strike",end=" ")
        if Ball_count:
            print(Ball_count, "Ball", end=" ")
        # 겹치는 값, 인덱스가 없는 경우 --> Strike값 Ball값이 모두 0이라면 아웃
        if Strike_count == 0 and Ball_count == 0:
            out_count   +=  1
            print("Out : 아웃 %d번"%out_count)            
        
        # 공백 출력
        print()

    
    # 시도횟수가 5라면 종료
    if try_count    >  5 :
        # 종료 안내문 출력
        print("게임횟수 초과")
        print("")
        print("게임횟수 초과")
    # 2아웃이면 종료

        # 종료 안내문 출력