# 검색어 : hello
# dhello dhellod hellod
# hello

# 입력 값
num = int(input("줄 수를 입력 하세요"))

textList = []

# 문장 입력
for index in range(num):
    textList.append(input(str(index + 1) + "번째 문장을 입력 하세요"))
    
# 검색어 입력
findWord = input("검색 단어를 입력 하세요")

for row in range(num):
    stateIndex = 0
    previousChar = ""
    nextChar = ""
    
    for col in range(len(textList[row])):
        nextChar = "" if col == (len(textList[row]) - 1) else textList[row][col+1]
        
        print("prev : ", previousChar, " cur : ", textList[row][col], " next : ", nextChar)
        # # 매칭 시작
        # if textList[row][col] == findWord[stateIndex] and stateIndex == 0:
        #     stateIndex += 1
        # # 매칭 중
        # elif textList[row][col] == findWord[stateIndex]:
        #     # 값 검색 완료
        #     if stateIndex == (len(findWord) - 1):
        #         print("검색, row, col : ", row, col)
        #         stateIndex = 0
        #     # 매칭 계속
        #     else:
        #         stateIndex += 1        
        # # 매칭 실패
        # else:
        #     stateIndex = 0
            
        previousChar = textList[row][col]