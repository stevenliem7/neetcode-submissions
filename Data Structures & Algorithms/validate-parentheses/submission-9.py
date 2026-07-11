class Solution:
    def isValid(self, s: str) -> bool:
        #()[]
        if len(s) <= 1:
            return False

        stack = []
        for val in s:
            if val == ']' and len(stack) > 0:
                if '[' not in stack[-1]:
                    return False
                else:
                    stack.pop()
            elif val == '}'and len(stack) > 0:
                if '{' not in stack[-1]:
                    return False
                else:
                    stack.pop()
            elif val == ')' and len(stack) > 0:
                if '(' not in stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(val)
        
        print("size" + str(stack) + str(len(stack)))
        if len(stack) == 0:
            return True
        return False
        