def solution(numbers):
    answer = []
    for indexA in range(len(numbers) - 1):              # 숫자 두 개 뽑아 더하기
        for indexB in range(indexA + 1, len(numbers)):
            
            value = numbers[indexA] + numbers[indexB]
            
            if value not in answer:                     # 중복되지 않는 값이면 추가
                answer.append(value)
                
    return sorted(answer)                               # 오름차순으로 반환