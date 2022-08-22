def solution(nums):
    sosuList = []
    
    for indexA in range(len(nums)):                                 # 첫 번째 수 뽑기
        
        for indexB in range(indexA + 1, len(nums)):                 # 두 번째 수 뽑기
            
            for indexC in range(indexB + 1, len(nums)):             # 세 번째 수 뽑기
                
                flag = True                                         # 스위치 ON
                sosu = nums[indexA] + nums[indexB] + nums[indexC]   # 확인할 수 정하기
                
                for value in range(2, int(sosu ** 0.5) + 1):        # 소수의 성질 -> 제곱근 보다 작은 수 중에 소인수가 없다
                    if sosu % value == 0:                           # 소인수 있으면 소수 아님
                        flag = False                                # 스위치 OFF
                        break                                       # 더 이상 반복할 필요 없음
                        
                if flag:                                            # 소수라면 스위치 ON 유지됨
                    sosuList.append(sosu)                           # 리스트에 추가

    return len(sosuList)                                            # (리스트의 길이) = (소수의 갯수)

print(solution([1,2,3,4]))