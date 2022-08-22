def solution(d, budget):
    d.sort()                    # 최대한 많은 부서를 지원해주기 위해 부서별로 필요한 돈을 정렬

    for index in range(len(d)):

        budget -= d[index]      # 부서별로 필요한 돈을 예산에서 뺀다.

        if budget < 0:
            return index        # 예산이 음수가 된다면 지원 종료

        elif budget == 0:       # 예산이 0이 된다면 지원 종료
            return index + 1

    return index + 1            # 예산이 남는다면 모든 부서에 지원한 것
        
###############################
# 다른 사람 답
def solution(d, budget):
    d.sort()
    
    while budget < sum(d):      # 예산이 부서별의 돈의 합보다 작을 때까지
        d.pop()                 # 큰 돈을 요하는 부서의 필요한 돈을 제거해준다.
        
    return len(d)               # 남은 원소들 반환