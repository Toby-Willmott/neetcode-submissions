class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_bracket = [] 
        stack_star = []
        for i, c in enumerate(s): 
            print(i,c)
            if c == "(":
                stack_bracket.append(i)
            elif c == "*":
                stack_star.append(i)
            else: 
                if stack_bracket:
                    print("yes")
                    stack_bracket.pop()
                elif stack_star:
                    stack_star.pop()
                else: 
                    return False     

        if stack_bracket and stack_star: 
            while stack_bracket and stack_star: 
                cur = stack_bracket.pop()
                index = stack_star.pop()
                if index <= cur: 
                    return False
        if stack_bracket: 
            return False
        return True
        

        