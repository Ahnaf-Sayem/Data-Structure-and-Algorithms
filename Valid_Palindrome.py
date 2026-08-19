class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []
        for letter in s:
            if letter.isalpha() == True or letter.isnumeric() == True:
                str.append(letter)

        str = ''.join(str)
        left = 0
        right =  len(str) - 1
        if len(str) > 0:

         while str[left].lower() == str[right].lower():
            if left ==  right:
                return True
            if left == right + 1:
                return True
            left += 1
            right -= 1
         return False
        else:
            return True

example = Solution()
print(example.isPalindrome("0P"))