def solution(N, stages):
    stageDict = {index : 0 for index in range(1, N + 1)}    # 각각의 스테이지 : 실패율
    stages.sort()                                           # 유저들의 현재 스테이지 오름차순 정렬

    userCount  = len(stages)                                # 총 유저의 명 수
    for value in range(1, N + 1):                           # 스테이지 확인
        valueCount = 0                                      # 통과못한 유저 수 담는 변수 선언

        if value in stages:                                 # 스테이지를 통과 못한 유저 있다면
            for compare in stages:                          # 찾기
                if compare > value:                         # 오름차순 -> 해당 스테이지 보다 높은 값이 나온다면
                    break                                   # 반복종료
                valueCount += 1 if compare == value else 0  # 카운트

        stageDict[value] = valueCount / userCount if userCount else 0.0 # 실패율 입력
        userCount -= valueCount                             # 카운트 된 만큼 유저수에서 빼기

    rangeValue = [value for value in stageDict.values()]    # 실패율을 가져오기
    rangeValue.sort(reverse = True)                         # 내림차순 정렬

    answer = []                                             # 답 담을 리스트 선언
    for value in rangeValue:                                # 실패율 가져오기
        for k, v in stageDict.items():                      # 딕셔너리 아이쳄 가져오기
            if v == value and k not in answer:              # 실패율에 맞는 스테이지 번호
                answer.append(k)                            # 답 리스트에 추가
    return answer


########### 다른 사람 답
# def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))