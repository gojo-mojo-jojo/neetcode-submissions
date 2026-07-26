class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_win = 0
        L = 0
        lut = set()
        for R in range(len(s)):
            while s[R] in lut:
                lut.remove(s[L])
                L +=1
            
            lut.add(s[R])
            max_win = max(max_win, R-L+1)
                #lut.remove(s[R])
                #L = R
        return max_win


        
        