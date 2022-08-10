# 학생 정보를 반환하는 함수 정의
def getinputValue(**informationOfStudent):
    inputValue = ''                                         # 학생 정보를 담을 변수 선언
    sum        = 0                                          # 학생 점수 합계를 담을 변수 선언
    
    for key,value in informationOfStudent.items():          # 학생 정보 담기
        inputValue += ' %s : '%key + str(value)
        
        if key == 'kor' or key == 'eng' or key == 'math' :  # 점수가 나오면 sum에 더해주기
            sum += value
    avg = sum / 3
    
    return avg, [inputValue + " sum : " + str(sum) + " avg : " + str(avg)]

# 값을 입력받는 함수 정의
def getValue(value):
    return input(value + "을 입력하세요\n")

inputValuelist   = []                                       # 입력데이터 담아줄 리스트
sumOfAvgs        = 0                                        # 평균값들의 합, 평균값들의 평균

while True:
    # 전체 평균 점수
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
        avg, inputValue =\
            getinputValue(id = getValue("학번"), name = getValue("이름"), kor = int(getValue("국어점수")), eng = int(getValue("영어점수")), math = int(getValue("수학점수")))

        inputValuelist.append(inputValue)
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