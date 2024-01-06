class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        if (not s): return True

        elif (length % 2 == 0): 
            mid = length // 2
            l, r = s[:mid], s[mid:][::-1]
        else:
            mid = length // 2 + 1 
            l, r = s[:mid - 1], s[mid:][::-1]

        return l == r

    def longestPalindrome(self, s: str) -> str:

        size = len(s)
        r = len(s) - size

        while (True):
            for i in range(r + 1):
                temp_s = s[i:i + size]
                if (self.isPalindrome(temp_s)):
                    return temp_s
            size -= 1
            r += 1        
        