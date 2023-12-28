class Solution:
    def __init__(self):
        self.romans = {
            1000: "M", 900: "CM",
            500: "D",  400: "CD",
            100: "C",  90: "XC",
            50: "L",   40: "XL",
            10: "X",   9: "IX",
            5: "V",    4: "IV",
            1: "I",
        }

    def intToRoman(self, num: int) -> str:
        
        output = ''

        for k in [key for key in self.romans.keys()]:

            while k <= num:
                output += self.romans[k]
                num -= k
        
        return output
        