class Solution:
    def __init__(self):
        self.is_negative = False
        self.has_sign = False
        self.sign = ["+", "-"]

    def rangeValidation(self, v):
        abs_range = 2 ** 31
        v_range = abs_range if self.is_negative else abs_range - 1
        return int(v) if int(v) < v_range else v_range

    def myAtoi(self, s: str) -> int:
        ss = ""

        for v in s:
            if v == " " and not ss:
                continue
            elif v in self.sign:
                if self.has_sign or ss: break
                self.has_sign = True
                self.is_negative = v == "-"
                ss += v
            elif v.isdigit():
                ss += v
            else:
                break

        if not ss or ss[0] in self.sign and len(ss) == 1:
            return 0

        num_str = ""
        i = 1 if ss[0] in self.sign else 0

        while i < len(ss) and ss[i].isdigit():
            num_str += ss[i]
            i += 1

        if not num_str:
            return 0

        num = self.rangeValidation(num_str)
        return -1 * num if self.is_negative else num
