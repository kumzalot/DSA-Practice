class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for c in s:
            if c in brackets.values(): # open paranthesis
                stack.append(c)
            elif c in brackets.keys():
                if stack and stack[-1] == brackets[c]: # close paranthesis
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False