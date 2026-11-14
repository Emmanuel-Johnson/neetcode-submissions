class Solution:
    def threeSum(self, og_nums: List[int]) -> List[List[int]]:
        nums = sorted(og_nums)
        result = []
        for i in range(1, len(nums) - 1):
            j, k = 0, len(nums) - 1
            while j < i < k:
                if nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                else:
                    if result and result[-1] == [nums[j], nums[i], nums[k]]:
                        break
                    result.append([nums[j], nums[i], nums[k]])
                    break
        return result