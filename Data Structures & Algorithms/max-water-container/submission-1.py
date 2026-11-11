class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = float('-inf')
        i, j = 0, len(height) - 1
        while i < j:
            result = max(result, (j - i) * min(height[i], height[j]))
            if height[i + 1] > height[j - 1]:
                i += 1
            else:
                j -= 1
            print(i, j)
        return result