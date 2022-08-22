def solution(n, lost, reserve):

    # 여벌 있는 사람이 도난당한 경우 없애주기
    newLost    = sorted([value for value in lost if value not in reserve])
    newReserve = sorted([value for value in reserve if value not in lost])

    # 여벌 받을 수 있는 경우 없애주기
    for value in newReserve:
        previousValue = value - 1   # 앞 사람
        nextValue     = value + 1   # 뒷 사람

        if previousValue in newLost:
            newLost.remove(previousValue)
        elif nextValue in newLost:
            newLost.remove(nextValue)

    return n - len(newLost)

print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))  