def solution(x, n):
    answer = []
    count = 0
    while True:
        count += 1
        if count > n:
            break
        answer.append(x*count)
    return answer

# def solution(x, n):
#     return [x+ x*n for n in range(n)]