class Solution:
    def topKFrequent(self, nums: List[int], top_k: int) -> List[int]:
        sorted_count = sorted(Counter(nums).items(), key=lambda x:-x[1])
        return [k for k, v in sorted_count][:top_k]