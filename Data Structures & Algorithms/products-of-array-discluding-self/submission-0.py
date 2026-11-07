class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        a, b = [1], [1]
        result = []
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            a.append(prefix)
        for i in range(len(nums) - 1, 0, -1):
            suffix *= nums[i]
            b.append(suffix)
        for i in range(len(a)):
            result.append(a[i] * b[len(b) - i - 1])
        return result