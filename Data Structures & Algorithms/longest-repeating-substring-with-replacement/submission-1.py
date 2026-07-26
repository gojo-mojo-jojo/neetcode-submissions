class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_len = 0

        L = 0
        max_freq = 0

        freq = {}
        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1
            max_freq = max(max_freq, freq[s[R]])
 
 

            if R - L  + 1 - max_freq > k:
                freq[s[L]] -= 1
                L += 1

            max_len = max(R - L  + 1, max_len)


        return max_len




        