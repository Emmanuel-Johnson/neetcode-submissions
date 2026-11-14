class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        result = []
        for i in range(1, len(nums) - 1):
            if nums[i] > 0:
                break
            j, k = 0, len(nums) - 1
            while j < i < k:
                if nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                else:
                    if (nums[i], nums[j], nums[k]) not in seen:
                        result.append([nums[j], nums[i], nums[k]])
                        seen.add((nums[i], nums[j], nums[k]))
                    j += 1
        return result