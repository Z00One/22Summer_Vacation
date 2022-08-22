def solution(n):
    for value in range(2, n):   # 1로 나누면 나머지가 안생김 -> 2부터 시작
        if n % value == 1:
            return value