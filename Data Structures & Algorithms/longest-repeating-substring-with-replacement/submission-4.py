class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        L = 0
        max_window = 0
        for R in range(len(s)):
            
            freq[s[R]] = freq.get(s[R], 0) + 1

            window = R - L + 1 

            while window - max(freq.values(), default=0) > k:
                freq[s[L]] -= 1
                L += 1
                window = R - L + 1
            
            max_window = max(max_window,window)
        return max_window


