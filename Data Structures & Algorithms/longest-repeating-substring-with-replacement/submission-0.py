class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        lut = {}
        max_len = 0
        L = 0
        max_freq = 0
        for R in range(len(s)):
            
            lut[s[R]] = lut.get(s[R], 0) + 1

            max_freq = max(max_freq, lut[s[R]])

            while R - L + 1 - max_freq > k:
                lut[s[L]] -= 1
                L += 1
            max_len = max(max_len,R - L + 1 )

        return max_len