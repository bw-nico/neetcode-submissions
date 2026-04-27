class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 1:
            n = n*-1
            while n > 0:
                ans*=x
                n-=1
            return 1/ans
        elif n == 0:
            return 1.0
        else:
            while n > 0:
                ans*=x
                n-=1
            return ans