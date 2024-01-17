class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        s = s.split()
        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            p = pattern[i]

            if p not in h.keys():
                if s[i] in h.values():
                    return False
                h[p] = s[i]

            if h[p] != s[i]:
                return False 

        return True