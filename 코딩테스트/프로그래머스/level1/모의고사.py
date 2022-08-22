def solution(answers):
    answerValues = ["12345", "21232425", "3311224455"]  # 3가지의 찍는 방식 리스트 선언
    returnValue  = []                                   # 정답 카운트 값을 담아줄 리스트 선언
    
    for value in answerValues:                          # 찍는 방법 하나씩 가져오기
        value = (value * len(answers))[:len(answers)]
        count = 0
        
        for index in range(len(answers)):               # 정답 카운트
            if answers[index] == int(value[index]):
                count += 1
            
        returnValue.append(count)                       # 카운트 값 담기
    
    # 가장 큰 카운트 수와 같은 수만 담기
    returnValue = [index + 1 for index in range(len(returnValue)) if sorted(returnValue)[-1] == returnValue[index]]
        
    return returnValue