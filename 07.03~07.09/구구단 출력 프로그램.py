
def gugudan() :
    flag = True
    while flag:
        #  1) 메뉴 우선 출력 후 키보드로부터 정수 값 입력
        print("-------------------------")
        print("1.","구구단 출력")
        print("2.","프로그램 종료")
        print("-------------------------")

        inputNumber = int(input(""))

    #  메뉴에서 “1”선택 시 구구단 출력, 
        if inputNumber == 1:
            while True:
                #  “구구단 출력” 메뉴 선택 시 출력 할 단을 키보드로부터 입력
                dan_num = int(input("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력"))
                #  출력 유효 단은 2 ~ 9
                #  9단 이외의 값이 들어올 경우 Error Msg. 출력 후 재입력
                if dan_num < 2 or dan_num > 9:
                    print("2~9사이 정수를 입력해주세요")
                    continue
                for num in range(1,10):
                    print(dan_num, "X", num, "=", dan_num * num)
                break
            
    # “2”인 경우 Msg. 출력 후 프로그램 종료
        elif inputNumber == 2:
            print("이용해주셔서 감사합니다")
            flag = False
    #  메뉴에서 “1” 또는 “2”이외의 값이 입력될 경우, Error Msg. 출력 후 재입력
        else:
            print("잘못 입력하셨습니다. 다시 입력하세요.")
            continue
