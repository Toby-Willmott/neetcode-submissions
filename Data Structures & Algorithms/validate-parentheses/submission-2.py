class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        convert = {")":"(", "}":"{", "]":"["}

        for char in s: 
            if char in convert:
                if stack and stack[-1] == convert[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack == []:
            return True
        else: 
            return False
        