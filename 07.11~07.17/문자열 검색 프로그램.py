# 몇 회 입력받을지 정하기
rangeValue  = int(input("입력 문자열의 줄(Line) 수를 입력하세요!"))
inputString      = []                                                 # 입력 받은 문자열을 저장할 리스트
line = []
searchValue = 0
allWord = 0
word = ""
for index in range(rangeValue):
    #  영문 문자열을 키보드로부터 입력 받아 리스트에 추가
    inputString.append(input("%d 번째 라인의 문자열을 입력하세요."%(index+1)))
    # 공백인 부분은 숫자로 바꿔주기

while True:
    word = input("검색 할 문자열을 입력하세요.")
    # 리스트에 없는 경우 값을 다시 받는다.
    if word in inputString:
        break
    else:
        word = input("찾을 수가 없습니다. 검색 할 문자열을 입력하세요.")
wordCapareValue = ""
# string의 요소들을 하나씩 찾아본다
for index in range(len(inputString)):
    wordCapareValue = ""
    # 어디서 나오는 지 확인
    if word in inputString[index]:
        # 검색된 라인 찾기
        line.append(index+1)
        blankCount = 0
        for value in inputString[index]:
            # 공백은 숫자    " "asdasd" "
            if value == " " :
                blankCount += 1
                wordCapareValue = ""

            if not(value.isdigit()):
                blankCount = 0
                wordCapareValue +=value

            # 얼마나 나오는 지 카운트
            if len(wordCapareValue) >= len(inputString[index]):

                if wordCapareValue == word:
                    searchValue += 1
                    allWord += 1
                    wordCapareValue = ""
                 
            if blankCount >= 1:
                if wordCapareValue == word:
                    searchValue += 1
                    allWord += 1
                    wordCapareValue = ""
                elif wordCapareValue == "":
                    allWord += 1

                
# 단어들 카운트
print(line)
print(searchValue)
print(allWord)

