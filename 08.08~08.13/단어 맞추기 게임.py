from random import randint

##### 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장하는 함수 정의
def getinputValue(COUNT = ['첫', '두', '세']):
    inputWords  = []                   # 입력 받은 단어 담아줄 리스트 선언
    
    for index in range(len(COUNT)):    # 단어 입력
        value = input(COUNT[index] + " 번째 단어를 입력하세요\n")
        
        while len(value) < 3 or len(value) > 20:    # 범위 내의 단어만 입력
            value = input("3이상 20이하 글자로 구성된 단어를 입력하세요\n")
        
        inputWords.append(value)
        index += 1
    
    return inputWords

##### 리스트 or 문자열 만들어주는 함수 정의
def getListOrString(rangeValue, list = True):
    if list:                                            # 리스트
        returnValue = [value for value in rangeValue]

    else:                                               # 문자열
        returnValue = ''
        for value in rangeValue:
            returnValue += value
    
    return returnValue

##### 선택된 단어의 글자 중 50%를 Blind 처리, Blind 처리 알파벳은 랜덤하게 선택하는 함수 정의
def blind(wordValue, BLINDRANGE = 2, BLIND = '_'):
    blindValueList  = getListOrString(wordValue)                    # 블라인드 처리할 단어의 리스트 선언
    rangeValue      =\
        (len(wordValue) // BLINDRANGE) if len(wordValue) % 2 == 0 else (len(wordValue) // BLINDRANGE) + 1 # 블라인드 처리할 범위

    for index in range(rangeValue):                                 # 블라인드 처리
        charIndex = randint(0, len(blindValueList) - 1)
        
        if blindValueList[charIndex] == BLIND:                      # 이미 블라인드 처리된 원소의 경우
            while blindValueList[charIndex] == BLIND:               # 블라인드 처리 안된 원소의 인덱스가 나올 때까지 반복
                charIndex = randint(0, len(blindValueList) - 1)

        blindValueList[charIndex] = BLIND
    
    blindValue      = getListOrString(blindValueList, list = False) # 블라인드 처리된 단어 선언
        
    return blindValueList, blindValue

########## main ##########
# 3개의 단어 중 한 개 단어를 임의 선택
selectedWord = getinputValue()[randint(0,2)]
print("단어 선택 완료 게임을 시작 합니다. 선택된 단어 :", selectedWord)

# 선택된 단어 블라인드 처리
blindWordList, blindWord = blind(selectedWord)

# 게임 시작
gameCount = 0
while True:
    gameCount += 1
    
    inputChar =\
        input(str(gameCount) + "번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요\n" + blindWord + "\n" )
    
    if inputChar in selectedWord:                   # 블라인드 제거
        for index in range(len(selectedWord)):      # 블라인드 제거할 인덱스 판별
            
            if selectedWord[index] == inputChar:    # 기존의 값으로 교체
                blindWordList[index] = inputChar
                blindWord = getListOrString(blindWordList, list = False)
    
    if "_" not in blindWord:                        # 정답
        print("Clear - 선택된 단어 :", selectedWord, "총 시도 횟수 :", gameCount)
        break