from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for i in word:
                key[ord(i)-ord('a')] += 1
            result[str(key)].append(word)
        return list(result.values())




