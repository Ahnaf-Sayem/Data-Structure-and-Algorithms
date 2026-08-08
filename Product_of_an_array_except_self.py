class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        product = 1
        for number in nums:
            product *= number
            prefix.append(product)
        product = 1
        for number in reversed(nums):
            product *= number
            suffix.append(product)
        index = 0
        suffix = suffix[::-1]
        final_list = []
        while True:
            if index == 0:
                final_list.append(suffix[index + 1])
            elif index == len(nums) - 1:
                final_list.append(prefix[index - 1])
                break
            else:
                product = prefix[index - 1] * suffix [index + 1]
                final_list.append(product)
            index += 1
        return final_list

obj = Solution()
obj.productExceptSelf([2,3,4,5])