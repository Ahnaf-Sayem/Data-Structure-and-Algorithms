class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for number in nums:
            if number -1 not in nums_set:
                length  = 1
                while (number + 1) in nums_set:
                    length += 1
                    number += 1
                longest = max(longest,length)
        print(longest)
obj = Solution()
obj.longestConsecutive([1,2,3,4,8,9,10,11,12])
