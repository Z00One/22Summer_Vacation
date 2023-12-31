class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        standard = strs[0]
        strs.remove(standard)
        output = ""

        for i in range(min_len):
            for s in strs:
                if standard[i] != s[i]:
                    return output
                
            output += standard[i]
        
        return output
