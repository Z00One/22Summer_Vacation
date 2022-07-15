##### 문자열 몇 개를 입력 받을 지 정하기
inputString = ["dhello    helloddd ddhello dddhelloddd", "    hello   djdhello hello", "hello dkdk hellodd"]                                                                # 입력된 문자열을 담을 리스트 선언

# input으로 값을 입력받는다
lineRange = int(input("입력 문자열의 줄(Line) 수를 입력하세요! "))

# 입력받은 값 만큼 반복한다
for index in range(lineRange):

    # 반복하면서 문자열을 입력받아 변수에 저장한다.
    inputString.append(input("%d 번쨰 라인의 문자열을 입력하세요. "%(index + 1)))

line = []                                                                       # 입력된 문자열이 있는 라인수를 담을 리스트 선언
allWord = []                                                                    # 전체 단어를 담아줄 리스트 선언
wordValue = ""                                                                  # 단어를 담기위한 변수 선언 
lineCheck = [0] * lineRange                                                     # 라인 체크를 위한 변수 선언

##### 전체 단어를 리스트에 넣어주기
for lineValue in range(lineRange):
    for index in range(len(inputString[lineValue])):
        ## 전체 단어 찾기
        # 공백인 경우
        if inputString[lineValue][index] == " ":

            # 문자열 뒤에 공백이 오는 경우  ex) "hello    "
            if wordValue:
                allWord.append(wordValue)
                if wordValue == searchString
                wordValue = ""

        # 공백이 아닌 경우
        else:
            wordValue += inputString[lineValue][index]

            # 마지막이 문자열로 끝나는 경우 ex) "         hello"
            if index == len(inputString[lineValue]) - 1:
                # 값이 존재한다면
                if wordValue:
                    allWord.append(wordValue)
                    lineCheck[lineValue] += 1

# 검색할 문자열 입력받기
searchString = input("검색 할 문자열을 입력하세요")                               # 검색할 문자열 선언
##### 어떤 문자열이 어디에 얼마나 있는지 특정
flag = True                                                                     # 반복 문의 수행 여부를 결정할 변수 선언

# 안에 검색할 문자가 안들어가 있는 동안 반복
while searchString not in allWord:
    searchString = input("찾을 수가 없습니다. 검색 할 문자열을 입력하세요. ")

print(searchString + "을 찾았습니다.")

# 라인체크 리스트의 벨류값만큼
# inputValue의 단어를 구분
# " "을 기준으로 나눈다.
for value in inputString:
    value
# 검색된 횟수 찾기
searchCount = 0                                                                       # 찾는 단어가 검색된 횟수를 담을 변수
for word in allWord:
    if word == searchString:
        searchCount += 1

# 검색된 라인 수, 검색된 횟수, 총 단어수 출력
print("검색된 라인 수 :",line)
print("검색된 횟수 :",searchCount)
print("총 단어 수 :",len(allWord))