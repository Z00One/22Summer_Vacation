class Solution:
    def __init__(self):
        self.romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    def romanToInt(self, s: str) -> int:
        output = 0
        len_s = len(s)
        prev_flag = False

        for c_i in range(len_s):
            c_v = self.romans[s[c_i]]
            n_v = self.romans[s[c_i + 1]] if c_i < len_s - 1 else 0
            
            if (prev_flag):
                p_v = self.romans[s[c_i - 1]]
                output += c_v - p_v
                prev_flag = False

            elif (c_v < n_v):
                prev_flag = True
                
            else:
                output += c_v
        
        return output