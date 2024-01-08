class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        li = []
        while k:
            t = k % 10
            k = (k-t) // 10
            li.insert(0,t)

        long_l = len(li) <= len(num)
        std_l = num if long_l else li
        std_s = li if long_l else num

        prev = 0
        for i in range(len(std_l) - 1, -1, -1):
            if std_s:
                temp = prev + std_l[i] + std_s[-1]
                del std_s[-1]
            elif not prev:
                break
            else:
                temp = prev + std_l[i]
            if 9 < temp:
                prev = 1
                std_l[i] = temp % 10
            else:
                prev = 0
                std_l[i] = temp
        
        if prev: std_l.insert(0, 1)
        
        return std_l
