class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        while nums:
            temp = []
            v = nums[0]
            while v in nums:
                temp.append(v)
                nums.remove(v)
                v += 1
            ranges.append(temp)
        
        ans = []
        for r in ranges:
            e = f"{r[0]}->{r[-1]}" if len(r) > 1 else str(r[0])
            ans.append(e)

        return ans