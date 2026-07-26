class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        max_L = 0
        max_R = 0
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    max_L = l
                    max_R = r
                l -= 1
                r += 1
            
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    max_L = l
                    max_R = r
                l -= 1
                r += 1
        
        return s[max_L:max_R+1]

            
        