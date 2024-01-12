class Solution:
    def toList(self, s: str, numRows: int):
        li = []
        std = [' ' for _ in range(numRows)]
        
        while True:
            for i in range(numRows - 1):
                if not s:
                    return li
                elif i == 0:
                    v = s[:numRows]
                    v += ' ' * (numRows - len(v))
                    li.append(v)
                    s = s[numRows:]
                else:
                    v = std[:]
                    v[numRows - i - 1] = s[0]
                    v = ''.join(v)
                    li.append(v)
                    s = s[1:]
    
    def flat(self, li: List[str], numRows: int) -> str:
        s = ''
        for i in range(numRows):
            for l in li:
                if l[i] != ' ':
                    s+=l[i]
        return s

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        li = self.toList(s, numRows)
        ans = self.flat(li, numRows)
        return ans