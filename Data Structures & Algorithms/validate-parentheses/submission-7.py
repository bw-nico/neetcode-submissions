class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        bracket_map = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        for each in s:
            if each in bracket_map:
                if open_stack and bracket_map[each] != open_stack[-1]:
                    return False
                elif open_stack:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(each)
        return not open_stack