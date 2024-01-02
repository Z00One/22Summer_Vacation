class Solution:
    def __init__(self):
        self.characters = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

    def isValid(self, s: str) -> bool:
        l_bs = []
        
        for b in s:
            if b in self.characters.keys():
                l_bs.append(b)
            else:
                if not l_bs or self.characters[l_bs.pop()] != b:
                    return False

        return len(l_bs) == 0
