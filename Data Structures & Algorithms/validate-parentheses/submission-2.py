class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        open_stack = []
        for bracket in s:
            if not bracket_dict.get(bracket):
                open_stack.append(bracket)
            else:
                if len(open_stack) > 0:
                    if bracket_dict.get(bracket) == open_stack[-1]:
                        open_stack.pop()
                    else:
                        return False
                else:
                    return False
        if open_stack == []:
            return True
        return False
        