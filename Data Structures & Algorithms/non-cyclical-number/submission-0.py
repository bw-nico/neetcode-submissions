class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while True:
            sum = 0
            for each in str(n):
                sum+=(int(each)**2)
            n = sum
            if sum in seen:
                return False
            elif sum == 1:
                return True
            seen.append(n)