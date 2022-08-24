def solution(progresses, speeds):
    answer = []
    # 가장 먼저 완료되어야 하는 프로젝트의 걸리는 일수
    dayValue = int(100 - progresses[0]) // speeds[0] + 1 if (100 - progresses[0]) % speeds[0] != 0 else int(100 - progresses[0]) // speeds[0]
    # 가장 앞에 있는 프로젝트가 완성되었을 때 나머지 프로젝트들의 완성도
    progresses = [progresses[index] + (dayValue * speeds[index]) for index in range(len(progresses))]

    for index in range(len(progresses)):        # 완성된 프로젝트 카운트
        if progresses[index] < 100:             # 미완성
            answer.append(index)
            progresses = progresses[index :]
            speeds     = speeds[index :]
            break

        if index == len(progresses) - 1:        # 전부 다 완성
            answer.append(len(progresses))
            progresses = []

    # 반복 말고 재귀
    return answer + solution(progresses, speeds) if progresses else answer

print(solution( [96,94],[3,3]))