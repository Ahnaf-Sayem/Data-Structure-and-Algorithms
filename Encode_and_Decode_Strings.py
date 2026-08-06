from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res = res + str(len(word)) + "#" + word
        return res
    def decode(self,s):
        i = 0
        res = []
        while i <len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1 + length
            res.append(s[j + 1: length + j + 1])
        return  res
a = Solution()
encoded = a.encode(['ahnaf'])
a.decode(encoded)