class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        visited = set()
        L = 0
        for R in range(len(s)):

            while s[R] in visited:
                visited.remove(s[L])
                L += 1

            visited.add(s[R])
            max_len = max(max_len, R-L+1)

        return max_len


