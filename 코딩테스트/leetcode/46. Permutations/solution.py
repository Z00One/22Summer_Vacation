class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def find(li, next_nums):
            if not next_nums:
                ans.append(li)
            
            for i in range(len(next_nums)):
                n = next_nums[i]
                find(li + [n], list(filter(lambda v: v != n, next_nums)))

        find([], nums)

        return ans
