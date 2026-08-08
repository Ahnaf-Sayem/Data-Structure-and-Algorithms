class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets_by_order = [set() for _ in range(len(nums))]
        nums_count = {} # number as a key and frequency as a value
        for number in nums:
            nums_count[number] = nums_count.get(number,0) + 1 # starts creating the nums_count
        for number in nums:
            buckets_by_order[nums_count[number] - 1].add(number) # it adds number based on frequency's ascending order through indices
        non_empty_buckets = [ bucket for bucket in buckets_by_order if bucket] # only none empty buckets to work on
        flattened_list = []
        for bucket in non_empty_buckets: # flattens the nested list but the order remains still
            for number in bucket:
                flattened_list.append(number)
        final_list = [] # final answer
        unique_frequency = 0
        frequency = 0
        for number in reversed(flattened_list):
            final_list.append(number)
            if nums_count[number] != frequency: # it cares about only number with unique frequency
                frequency = nums_count[number]
                unique_frequency += 1
            if unique_frequency == k:# stops when k number of unique frequency numbers are found
                break
        return final_list
a =  Solution()
a.topKFrequent([1,2,2,4,4,6,7,7,7],3)