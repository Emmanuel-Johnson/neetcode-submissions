class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        for f, s in count.items():
            if s >= k:
                result.append(f)
        return result