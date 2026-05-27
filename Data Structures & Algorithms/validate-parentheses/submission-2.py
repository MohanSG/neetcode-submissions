class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        matches = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] =="{":
                brackets.append(s[i])
            elif brackets and matches[s[i]] == brackets[-1]:
                brackets.pop(-1)
            else:
                return False
        
        if brackets:
            return False
        else:
            return True