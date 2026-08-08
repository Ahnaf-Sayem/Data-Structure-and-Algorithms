from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for number in nums:
            nums_count[number] = nums_count.get(number, 0) + 1

        buckets = [set() for _ in range(len(nums))]
        for number, freq in nums_count.items():
            buckets[freq - 1].add(number)

        non_empty_buckets = [bucket for bucket in buckets if bucket]

        final_list = []
        for bucket in reversed(non_empty_buckets):
            for number in bucket:
                final_list.append(number)
                if len(final_list) == k:
                    return final_list

        return final_list