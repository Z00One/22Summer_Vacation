class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        # 모든 수를 탐색. 마지막 두 수는 이미 포인터로 확인.
        for i in range(len(nums)-2):

            # 현재 수가 이전 수와 같다면 중복되는 결과를 방지.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 두 개의 포인터를 설정.
            l, r = i+1, len(nums)-1
            
            # 포인터가 만나기 전까지 반복.
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                
                else:  # 합이 0이라면 결과를 추가.
                    output.append((nums[i], nums[l], nums[r]))
                    # 왼쪽 포인터가 가리키는 수가 다음 수와 같다면 건너뜀.
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # 오른쪽 포인터가 가리키는 수가 이전 수와 같다면 건너뜀.
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1; r -= 1
                    
        return output