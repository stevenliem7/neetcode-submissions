class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = 0
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        for elem in tokens:
            if elem not in ["+", "-", "*", "/"]:
                stack.append(elem)
            else:
                # Check if we are at the bottom first
                temp2, temp1 = int(stack.pop()), int(stack.pop())

                # Handle math ops
                if elem == "+":
                    curr = temp1 + temp2
                elif elem == "-":
                    curr = temp1 - temp2
                elif elem == "*":
                    curr = temp1 * temp2
                else:
                    curr = temp1 / temp2


                stack.append(curr)
            
        return int(curr)
            