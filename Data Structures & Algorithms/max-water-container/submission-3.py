class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = float("-inf")
        i, j = 0, len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            result = max(result, (j - i) * min(height[i], height[j]))
            if i < j and height[i] <= h:
                i += 1
            if i < j and height[j] <= h:
                j -= 1
        return result