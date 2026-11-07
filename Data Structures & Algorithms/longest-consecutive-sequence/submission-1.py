class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen, result = set(nums), 0
        for num in nums:
            count, current = 0, num
            if num - 1 not in seen:
                while current in seen:
                    count += 1
                    current += 1
                result = max(count, result)
        return result