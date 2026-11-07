class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, prefix, suffix = [""] * len(nums), 1, 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result