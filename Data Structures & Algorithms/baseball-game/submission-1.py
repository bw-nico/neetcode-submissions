class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        score = 0
        for op in operations:
            if op == "+":
                score += score_stack[-1] + score_stack[-2]
                score_stack.append(score_stack[-1] + score_stack[-2])
            elif op == "D":
                score += (score_stack[-1] * 2)
                score_stack.append(score_stack[-1] * 2)
            elif op == "C":
                score -= score_stack[-1]
                score_stack.pop()
            else:
                score += int(op)
                score_stack.append(int(op))
        return score

        