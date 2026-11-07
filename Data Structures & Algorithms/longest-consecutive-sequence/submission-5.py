class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen, result = set(nums), 0
        for num in nums:
            if num - 1 not in seen:
                count, current = 0, num
                while current in seen:
                    count += 1
                    current += 1
                result = max(result, count)
        return result