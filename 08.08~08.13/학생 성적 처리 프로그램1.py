inputValuelist   = []         # 입력데이터 담아줄 리스트
sumOfAvgs        = 0          # 평균값들의 합, 평균값들의 평균

def getAvgValues(list):
    avg = sumOfAvgs/len(list) if len(list) != 0 else 0.0

def getinputValue(*informationOfStudent):
    inputValue = ''
    for value in informationOfStudent:
        inputValue += ' informationOfStudent : ' + str(informationOfStudent)
    inputValuelist.append([inputValue])
while True:
    avgOfAvgs  = \
        sumOfAvgs/len(inputValuelist) if len(inputValuelist) != 0 else 0.0
    # 기본 출력 메시지
    print("============================")
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력(입력 순)")
    print(" 3. 프로그램 종료")
    print("현 입력데이터 갯수 :", len(inputValuelist))
    print("전체 학생 평균 값  :", avgOfAvgs)
    print("============================")

    # 선택
    selectValue = input("")
    # 1 학생 성적 입력
    if selectValue == '1':
        id   = input("학번을 입력하세요\n")
        name = input("이름을 입력하세요\n")
        kor  = int(input("국어 성적을 입력하세요\n"))
        eng  = int(input("영어 성적을 입력하세요\n"))
        math = int(input("수학 성적을 입력하세요\n"))
        sum  = kor + eng + math
        avg  = sum / 3

        inputValuelist.append(['id : ' + id + ' name : ' + name + ' kor : ' + str(kor) + ' eng : ' + str(eng) + ' math : ' + str(math) + ' sum : ' + str(sum) + ' avg : ' + str(avg)])
        sumOfAvgs += avg

    # 2 학생 목록 출력
    elif selectValue == '2':
        for studentList in inputValuelist:
            print(studentList)
        
    # 3 프로그램 종료
    elif selectValue == '3':
        break
    
    # 4 예외처리
    else:
        selectValue = input("선택할 수 있는 값을 입력하세요")