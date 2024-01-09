class Solution:
    def __init__(self):
        self.phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = ['']

        for digit in digits:
            temp = []
            for ans_part in ans:
                for letter in self.phone[digit]:
                    temp.append(ans_part + letter)
            ans = temp

        return ans