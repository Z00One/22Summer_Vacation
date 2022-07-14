def solution(n):
    n = list(str(n))
    # 문자열로 형 변환 후 리스트에 넣어서 요소별로 돌린다
    for element1 in range(len(n) - 1):
        for element2 in range(element1+1, len(n)):
            # 자기보다 큰 수가 있으면 뒤로간다.
            if n[element2] > n[element1]:
                temp = n[element2]
                n[element2] = n[element1]
                n[element1] = temp
    n = "".join(n)
    return '"%s"'%n
print(solution(118372))