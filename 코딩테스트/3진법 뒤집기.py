def solution(n):
    # 10진법 -> 3진법
    n3  = []    # 3진법의 자릿수들을 담아줄 리스트
    while n:    # n이 0이 될 때(다 나누어질 때)까지
        n3.append(n % 3)     # 3진법의 자릿수 추가
        n = n // 3
    
    # 3진접 앞뒤 반전  -> 10진법 
    for index in range(len(n3)):
        if n3[len(n3) - 1 - index]:                             # 앞뒤 반전했을 때 해당하는 값이 있을 경우 연산
            n10 += n3[len(n3) - 1 - index] * (3**index)         # 자릿수와 자리에 맞는 3의 승수를 곱한 값을 더해준다.

    return n10

#################### 다른 사람 답
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)  # int(str, int) : str값이 int진법 에서 10진법으로 바뀐 값을 반환
#     return answer

print(solution(45))