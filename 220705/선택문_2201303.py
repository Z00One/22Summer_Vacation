flag = True
input_count = 1
Msg = ""
while flag:
    #  키보드로부터 정수 값 입력
    input_Value = int(input(""))

    #  “1” 이상의 값만 입력, “0” 이하의 값 입력 시 아래 Msg 출력 후 재입력
    if input_Value < 1:
        Msg = "1이상 양수를 입력해주세요"
        print(Msg)
        continue

    #  ‘20,000’ 입력 시 아래 Msg 출력 후 프로그램 종료
    elif input_Value == 20000:
        Msg = "이용해주셔서 감사합니다"
        print(Msg)
        flag = False

    else:
    #  현재 입력 횟수 출력 후 키보드 입력 값 화면에 출력
        Msg = str(input_count)+"번째 입력 값은 ="
        print(Msg, input_Value)
        #  “짝수”or “양수” 출력
        if input_Value % 2 == 0:
            Msg = "짝수 입니다."
            print("\t" + Msg)
        #  3의 배수 또는 7의 배수이면 아래 Msg 출력

            if input_Value % 3 == 0:
                Msg = "3의 배수 입니다."
                print("\t" + Msg)

            elif input_Value % 7 == 0:
                Msg = "7의 배수 입니다."
                print("\t" + Msg)

            input_count+=1

        #  “짝수”or “양수” 출력        
        elif input_Value % 2 == 1:
            Msg = "홀수 입니다."
            print("\t" + Msg)
        #  3의 배수 또는 7의 배수이면 아래 Msg 출력
            if input_Value % 3 == 0:
                Msg = "3의 배수 입니다."
                print("\t" + Msg)

            elif input_Value % 7 == 0:
                Msg = "7의 배수 입니다."
                print("\t" + Msg)

            input_count+=1



