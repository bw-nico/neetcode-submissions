class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left]
            right_char = s[right]
            if left_char.isalnum() and right_char.isalnum():
                if left_char.lower() != right_char.lower():
                    return False
                else:
                    left+=1
                    right-=1
            elif not left_char.isalnum():
                left+=1
            else:
                right-=1
        return True
        