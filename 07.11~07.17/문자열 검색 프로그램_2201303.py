rangeValue       =  int(input("입력 문자열의 줄(Line) 수를 입력하세요!"))               # 몇 회 입력받을지 정하기
inputString      =  []                                                                  # 입력 받은 문자열을 저장할 리스트 선언
allWord          =  []                                                                  # 단어들을 담아줄 리스트 선언
inputString = ["dhello    helloddd ddhello dddhelloddd", "    hello   djdhello hello", "hello dkdk hellodd"]                                                                # 입력된 문자열을 담을 리스트 선언

# for index in range(rangeValue):
#     #  영문 문자열을 키보드로부터 입력 받아 리스트에 추가
#     inputString.append(input("%d 번째 라인의 문자열을 입력하세요."%(index+1)))

# 검색할 문자열 받기
flag             =  True                                                                # 반복 여부 결정 변수 선언
searchString     =  input("검색 할 문자열을 입력하세요.")                               # 검색할 값 정하기
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

# inputString의 요소들을 하나씩 찾아본다
line             =  [0] * rangeValue                                                                 # 검색한 문자열이 있는 라인 담아줄 리스트 선언 
Word = ""
for index in range(len(inputString)):
   
    # 단어들 담아주기
    for indexChar in range(len(inputString[index])):

        # 공백이 아닐 때
        if not(inputString[index][indexChar] == " "):
            Word += inputString[index][indexChar]
        
        else: # 공백일 때
            if Word: # 값이 있다면
                allWord.append(Word)
                if Word == searchString:
                    line[index] = index + 1
                Word=""

        # 마지막이 문자열로 끝나고 Word에 값이 있을 때
        if indexChar == len(inputString[index]) - 1 and Word != "":
            allWord.append(Word)
            if Word == searchString:
                line[index] = index + 1
            Word=""

# 검색된 횟수
searchCount = 0
for value in allWord:                   # 전체 단어에서 찾으려는 단어 찾기
    if value == searchString:
        searchCount += 1

for lineValue in line:
    if lineValue == 0 :
        line.remove(lineValue)
# 값 출력하기
print("%s를 찾았습니다."%searchString)
print("검색된 라인 수:", line)

# for index in range(len(line)) :
#     if len(line) ==1 :                  # 라인리스트의 원소가 하나일 때
#         print(line[index])
#     elif index == len(line) - 1 :       # 마지막 원소일 때
#         print(line[index])
#     else:                               # 둘 다 아닐때
#         print(line[index],",",end=" ")

print("검색된 횟수 :", searchCount)
print("총 단어 수 :", len(allWord))