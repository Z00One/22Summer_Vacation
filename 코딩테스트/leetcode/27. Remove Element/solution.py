class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        while val in nums:
            nums.remove(val)
            nums.append('_')
            c += 1    
        
        return len(nums) - c
