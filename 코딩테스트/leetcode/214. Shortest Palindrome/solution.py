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

    def shortestPalindrome(self, s: str) -> str:
        i = -1
        temp = ""
        temp_s = s

        while not self.isPalindrome(temp_s):
            temp += s[i]
            temp_s = temp + s
            i -= 1
        
        return temp_s