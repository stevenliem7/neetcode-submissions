class Solution:
    def isValid(self, s: str) -> bool:
        #()[]
        if len(s) <= 1:
            return False

        stack = []
        for val in s:
            s_length = len(stack)
            if val == ']' and s_length> 0:
                if '[' not in stack[-1]:
                    return False
                else:
                    stack.pop()
            elif val == '}'and s_length > 0:
                if '{' not in stack[-1]:
                    return False
                else:
                    stack.pop()
            elif val == ')' and s_length > 0:
                if '(' not in stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(val)
        
        if len(stack) == 0:
            return True
        return False
        