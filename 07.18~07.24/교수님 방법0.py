rangeValue = int(input("줄 수를 입력하세요"))

stringList = []

for index in range(rangeValue):
    stringList.append(input(str(index + 1)+"번째 값을 입력하세요."))

findString = input("찾는 값을 입력하세요.")

previousChar   =  ""    # 이전값
nextChar       =  ""    # 다음값
searchedCount  =  0
allStringCount =  0
line           = [0] * rangeValue

while not(searchedCount):
    for stringIndex in range(len(stringList)):
        stateIndex     =  0     # 매칭하려는 값과 같은 값인지 확인하기 위한 변수 선언
        for charIndex in range(len(stringList[stringIndex])):
            # 다음값
            nextChar = "" if charIndex == len(stringList[stringIndex])-1 else stringList[stringIndex][charIndex + 1]
            # 단어 새기
            if not(previousChar.isalpha()) and stringList[stringIndex][charIndex].isalpha():
                allStringCount += 1

            # 매칭 시작
            if not(previousChar.isalpha()) and stringList[stringIndex][charIndex] == findString[stateIndex] and stateIndex == 0:
                # 맞든 안맞는 단어다.
                stateIndex     += 1
            
            # 매칭 중
            elif stringList[stringIndex][charIndex] == findString[stateIndex] :
                # 끝내기
                if stateIndex == len(findString) - 1 and not(nextChar.isalpha()):
                    stateIndex = 0
                    searchedCount += 1
                    line[stringIndex] = stringIndex + 1
                # 값이 다 맞는데 뒤에 또 문자열이 나올 때
                elif stateIndex == len(findString) - 1 and nextChar.isalpha():
                    stateIndex = 0
                # 계속 진행
                else : 
                    stateIndex += 1

            # 매칭 실패
            else:
                stateIndex = 0
            # 이전 값
            previousChar = stringList[stringIndex][charIndex]
    # 찾는 값이 없다면
    if not(searchedCount):
        findString = input("찾는 값이 없습니다. 다시 입력하세요")

# 값이 나오지 않은 라인 원소 제거
while 0 in line:
    line.remove(0)

print(allStringCount , searchedCount, line)