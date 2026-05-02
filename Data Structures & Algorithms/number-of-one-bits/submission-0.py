class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            # Check if the last bit is 1
            count += (n & 1)
            # Shift everything to the right by 1
            n >>= 1
        return count
        