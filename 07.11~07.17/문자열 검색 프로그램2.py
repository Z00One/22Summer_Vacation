lineRange        =  int(input("입력 문자열의 줄(Line) 수를 입력하세요!"))          # 몇 회 입력받을지 정하기
inputString      =  []                                                          # 입력 받은 문자열을 저장할 리스트 선언
allWord          =  0                                                           # 단어들을 담아줄 리스트 선언

# 입력받은 값 만큼 반복한다
for index in range(lineRange):
    #  영문 문자열을 키보드로부터 입력 받아 리스트에 추가
    inputString.append(input("%d 번째 라인의 문자열을 입력하세요."%(index+1)))

## 검색할 문자열 받기
flag             =  True                                                        # 반복 여부 결정 변수 선언
searchString     =  input("검색 할 문자열을 입력하세요.")                         # 검색할 값 정하기

while flag:
    # 리스트 전체를 다 돈다
    for index in range(len(inputString)):
        # 하나라도 찾으면 break
        if searchString in inputString[index]:                                      
            flag = False
            break
    # 못찾으면 값 다시 입력
    if flag:
        searchString = input("찾을 수가 없습니다. 검색 할 문자열을 입력하세요.")

## inputString의 요소들을 하나씩 찾아본다
searchCount      =   0                                                        # 찾는 문자열이 있는 지 카운트할 변수 선언
line             =   [0] * lineRange                                           # 검색한 문자열이 있는 라인 담아줄 리스트 선언 
word             =   ""                                                        # 단어를 담아줄 변수 선언
for index in range(len(inputString)):
   
    # 단어들 담아주기
    for indexChar in range(len(inputString[index])):

        # 공백이 아닐 때
        if not(inputString[index][indexChar] == " "):
            word += inputString[index][indexChar]   # 문자 담아주기
        
        # 공백일 때
        else:                                   
            if word:                                # 값이 있다면
                allWord += 1                # 단어로 추가
                if word == searchString:            # 값이 찾는 값과 같다면
                    searchCount += 1                # 검색횟수 추가
                    line[index] = index + 1         # 라인 추가
                word=""

        # 마지막이 문자열로 끝나고 Word에 값이 있을 때
        if indexChar == len(inputString[index]) - 1 :
            if word:                                # 값이 있다면
                allWord += 1                # 단어로 추가
                if word == searchString:            # 값이 찾는 값과 같다면
                    line[index] = index + 1         # 검색횟수 추가
                    searchCount += 1                # 라인 추가
                word=""

# 라인 값이 0 인 부분은 삭제
while 0 in line:
    line.remove(0)

# 값 출력하기
print("%s를 찾았습니다."%searchString)
print("검색된 라인 수:", line)
print("검색된 횟수 :", searchCount)
print("총 단어 수 :", allWord)