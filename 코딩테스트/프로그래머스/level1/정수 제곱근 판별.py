def solution(n):
    x = n**(1/2)
    # n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴 아니라면 -1을 리턴
    return int((x+1)**2) if n % x == 0 else -1
print(solution(121))
