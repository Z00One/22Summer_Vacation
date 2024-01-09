class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        can = list(filter(lambda x: x < target, candidates)) # target 보다 작은 수만 받기
        
        def find(v, li):
            if v > target:
                return
            elif v < target:
                for c in can:
                    if c > v or (li and c >= li[-1]): # 중복 피하기
                        find(v+c, li + [c])
            else:
                ans.append(li)
                return
        find(0, [])

        if target in candidates: ans.append([target])
        
        return ans
