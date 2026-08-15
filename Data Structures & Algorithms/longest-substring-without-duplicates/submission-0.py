class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        highest = 0
        valid = 0
        tracker = {}

        for i, ch in enumerate(s):
            if ch in tracker:
                valid = max(valid, tracker[ch] + 1)

            tracker[ch] = i
            highest = max(highest, i - valid + 1)

        return highest