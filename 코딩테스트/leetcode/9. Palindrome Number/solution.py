class Solution:
    def isNegative(self, x: int) -> bool:
        return x < 0

    def makeToString(self, x: int) -> str:
        return str(x)
        
    def isPalindrome(self, x: int) -> bool:
        if self.isNegative(x):
            return False
        
        str_x = self.makeToString(x)
        return str_x == str_x[::-1]