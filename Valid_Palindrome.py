class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.Is_alpha_numeric(s[l]):
                l += 1
            while l < r and not self.Is_alpha_numeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
        return True
    def Is_alpha_numeric(self,c):
        return (ord('a') <= ord(c.lower()) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
example = Solution()
print(example.isPalindrome("           "))