class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        output = 0
        for i in range(len(nums) - 2):

            l, r = i + 1 , len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1
                
                if(not(output) or abs(output - target) >= abs(s - target)):
                    output = s
                
        return output