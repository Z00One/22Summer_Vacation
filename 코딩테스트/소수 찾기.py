def solution(n):
    sosuList = [2]                          # n은 2이상의 수 -> 2는 시작부터 소수 리스트에 넣어도 상관없음
    for value in range(3, n + 1, 2):        # 2는 리스트 안에 있음 -> 3부터 확인
        flag = True                         # 스위치 ON

        for sosu in sosuList:               # 소수의 성질 -> 소수로 나눠지지 않으면 소수

            if sosu > int(value ** 0.5):    # 소수의 성질 -> 제곱근 보다 작은 소수들로 안나눠지면 소수
                break

            if value % sosu == 0:           # 나눠진다면 소수 아님
                flag = False                # 스위치 OFF
                break

        if flag:                            # 소수 리스트에 추가
            sosuList.append(value)

    return len(sosuList)                    # 소수의 갯수 = 리스트의 길이

########## 다른 사람 답
def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)

print(solution(10))