class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:

            result["".join(sorted(i))].append(i)

        return [v for k, v in result.items()]