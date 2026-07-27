class Solution:
    def checkValidString(self, s: str) -> bool:

        cache = {}
        def  dfs(i, left_open):
            if i == len(s):
                return left_open == 0
            if (i, left_open) in cache:
                return cache[(i, left_open)]
            if left_open < 0 :
                return False


            if s[i] == '(':
                result = dfs(i+1, left_open+1)
            elif s[i] == ')':
                result = dfs(i+1, left_open-1)
            else: 
                result =  dfs(i+1, left_open) or dfs(i+1, left_open+1) or dfs(i+1, left_open-1)
            cache[(i, left_open)] = result
            return cache[(i, left_open)]
        
        return dfs(0, 0)


