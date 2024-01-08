class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = str(int(a) + int(b))

        ans = ''
        prev = 0

        for v in c[::-1]:
            temp = prev + int(v)
            if 1 < temp:
                prev = 1
                ans = str(temp%2) + ans
            else:
                prev = 0
                ans = str(temp) + ans

        return '1' + ans if prev else ans            
