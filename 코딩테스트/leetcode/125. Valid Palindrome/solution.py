class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for v in s:
            if v.isalnum():
                ss += v.lower()
        leng = len(ss)
        l = ss[:leng // 2][::-1]
        r = ss[leng // 2:] if (leng % 2 == 0) else ss[leng // 2 + 1:]
        return l == r
