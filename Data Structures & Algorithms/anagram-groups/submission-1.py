class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        result = defaultdict(list)
        for i in strs:
            if i not in seen:
                seen.add("".join(sorted(i)))
                result["".join(sorted(i))].append(i)
            else:
                result["".join(sorted(i))].append(i)
        return [v for k, v in result.items()]