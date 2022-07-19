rangeValue = int(input("줄 수를 입력하세요"))

stringList = []

for index in range(rangeValue):
    stringList.append(input(str(index + 1)+"번째 값을 입력하세요."))

findString = input("찾는 값을 입력하세요.")

searchedCount  =  0
line           = [0] * rangeValue

while not(searchedCount):
    allStringCount =  0

    for stringIndex in range(len(stringList)):
        previousChar   =  ""    # 이전값
        nextChar       =  ""    # 다음값
        stateIndex     =  0     # 매칭하려는 값과 같은 값인지 확인하기 위한 변수 선언
        for charIndex in range(len(stringList[stringIndex])):
            # 다음값
            nextChar = "" if charIndex == len(stringList[stringIndex])-1 else stringList[stringIndex][charIndex + 1]

            # 단어 새기 -- 계속 하나가 빠진다.
            if not(previousChar.isalpha()) and stringList[stringIndex][charIndex].isalpha():
                allStringCount += 1
        

            # 매칭 시작
            if not(previousChar.isalpha()) and stringList[stringIndex][charIndex] == findString[stateIndex] and stateIndex == 0:
                stateIndex     += 1

                # 찾는 글자가 한 글자인 경우
                if len(findString) == 1:
                    # 앞 뒤로 문자가 없을 때만
                    stateIndex = 0
                    if not(previousChar.isalpha()) and not(nextChar.isalpha()):
                        searchedCount += 1
                        line[stringIndex] = stringIndex + 1
            
            # 매칭 중
            elif stringList[stringIndex][charIndex] == findString[stateIndex] and previousChar.isalpha() and stateIndex != 0 :
                # 끝내기
                if stateIndex == len(findString) - 1:

                    # 찾는 글자가 하나인 경우
                    if len(findString) == 1 and not(nextChar.isalpha()) and not(previousChar.isalpha()):
                        searchedCount += 1
                        line[stringIndex] = stringIndex + 1

                    # 찾는 글자가 여러개인 경우
                    elif not(nextChar.isalpha()):
                        searchedCount += 1
                        line[stringIndex] = stringIndex + 1
                    stateIndex = 0

                # 값이 다 맞는데 뒤나 앞에 문자열이 나올 때
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