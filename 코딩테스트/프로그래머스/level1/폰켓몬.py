def solution(nums):
    newNums    = len(set(nums))         # 중복 제거
    count      = len(nums) // 2         # 고를 수 있는 폰켓몬 수

    answer = count if count < newNums else newNums
    return answer