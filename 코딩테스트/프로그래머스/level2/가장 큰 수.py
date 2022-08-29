# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수 만들기
def solution(numbers):
    numbers = sorted([str(num) for num in numbers])
    numbers.sort(key = len)
    compareValue     = len(numbers[-1])
    # numbers.sort(reverse=True)
    
    numbersDict = {key : int((key * compareValue)[:3]) for key in numbers}
    compare     = [num for num in numbersDict.values()]
    compare.sort(reverse=True)

    answer = ''
    for num in compare:
        for key, value in numbersDict.items():
            if num == value:
                answer += key
                numbersDict[key] = 0
                break
    
    return answer
    
    # compareList = []
    # for indexA in range(len(numbers)):
    #     compare = []

    #     for indexB in range(indexA + 1, len(numbers)):

    #         if numbers[indexA] == numbers[indexB][0]:
    #             compare.append(numbers[indexB])

    #         else: break
        
    #     if compare:
    #         compare.append(numbers[indexA])
    #         compareList.append(compare)
        
    # numbers = numbers[len(compare)]
    
    # return numbers
print(solution( [ 67,676,677,]))
    