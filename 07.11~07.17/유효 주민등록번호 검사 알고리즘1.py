sum        =  0     # a 값을 더해줄 변수 sum 선언
checkValue =  2     # 체크값 선언

# 주민등록번호를 입력받기
myNum = input("주민번호를 입력하세요")
# 입력값을 리스트로 for 문을 돌리기 --> 마지막 요소가 아닌 숫자만 연산 해주기 --> 리스트 조정, 숫자 판별 필요
for index in range(len(myNum)-1):
    
    # 숫자라면 진행 아니라면 다음 반복
    if not(myNum[index].isdigit()):
        continue

    # sum에 a 값을 추가
    # 입력한 주민등록번호의 각 자리 마다 체크수를 곱해주기  --a             
    sum += int(myNum[index]) * checkValue

    # 체크 수는 반복 마다 바뀌게 하기
    checkValue += 1

    # 체크수는 10 되면 다시 2로 바뀐다.
    if checkValue == 10:
        checkValue = 2

## 11 - (sum % 11) 값이 마지막 자리 값과 같은 경우
## 11 - (sum % 11) 값이 두 자릿수가 나온다면 10으로 나눈 나머지 값과 마지막 자리값이 같은 경우
judgeValue = 11 - (sum % 11)

# judgeValue 가 두자릿수일 경우 일의 자리수만 이용
if judgeValue >= 10:
    judgeValue -= 10 # or %= 연산자 사용

## judgeValue가 마지막 자릿수랑 같은 경우
if judgeValue == int(myNum[-1]) :
    # "유효한 주민번호 입니다." 출력
    print("유효한 주민번호 입니다.")

## 아닌 경우
else :
    # "유효하지 않은 주민번호 입니다." 출력
    print("유효하지 않은 주민번호 입니다.")