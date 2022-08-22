# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수 만들기
def solution(numbers):
    numbers = sorted([str(num) for num in numbers])
    numbers.sort(key = len)
    
    numbersDict = {key : int((key * len(numbers[-1]))[:len(numbers[-1])]) for key in numbers}
    compare     = [int((num * len(numbers[-1]))[:len(numbers[-1])]) for num in numbers]
    compare.sort(reverse=True)

    answer = ''
    for num in compare:
        for key, value in numbersDict.items():
            if num == value and key in numbers:
                answer += key
                numbers.remove(key)
    
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
print(solution([3, 3, 333, 34]))
    