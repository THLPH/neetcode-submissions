from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        for key in nums:
            result[key] += 1

        return sorted(result, key=result.get, reverse=True)[:k]