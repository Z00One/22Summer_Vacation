class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1

        h = [v for v in haystack]
        std = needle[0]
        
        while True:
            idx = h.index(std)
            if (needle == haystack[idx:idx+len(needle)]):
                return idx
            h[idx] = '_'