def solution(numbers):
    answer    = ''
    dictNum   = {}
    newNum    = []
    
    for value in numbers:                               # 숫자 두 개의 리스트로 분리하기
        if value > 9:                                   # n자릿수 (n >= 2)
            newNum.append(value)
            
            if int(str(value)[0]) in numbers and int(str(value)[0]) not in newNum:           # n자릿수의 첫번째 자리 값
                newNum.append(int(str(value)[0]))
            
    numbers.sort(reverse = True)                        # 한자릿수 리스트 내림차순 정렬
    
            
    for index in range(len(newNum)):                    # {모든자릿수 합 : 숫자} 딕셔너리 만들기
        
        if newNum[index] in numbers:
            numbers.remove(newNum[index])
        
        if newNum[index] > 9:                           # 두자릿수
            newValue = 0
            
            for value in str(newNum[index]):
                newValue += int(value)
            
            dictNum[newValue]      = newNum[index]      # 기존의 리스트 값을 모든자릿수 합으로 바꾸기
            newNum[index]          = newValue
        
        else:
            dictNum[newNum[index]] = newNum[index]      # 한자릿수
            
    newNum.sort(reverse = True)                         # 내림차순 정렬
    
    for value in newNum:                                # 큰 순서대로 문자열로 붙혀주기
        answer += str(dictNum[value])
        
    return answer

print(solution([3, 30, 34, 5, 9]))