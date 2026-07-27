class Solution:
    def checkValidString(self, s: str) -> bool:

        leftmin, leftmax = 0, 0 #to track the decision * 

        for c in s:
            if c == '(':
                leftmin += 1
                leftmax  += 1

            elif c == ')':
                leftmin -= 1
                leftmax -= 1

            else: # if *
                leftmin -= 1
                leftmax += 1
            
            if leftmax < 0:
                return False # ')' came before '('
            
            if leftmin < 0: 
                leftmin = 0 # can be balanced by leftmax tracking *

        return leftmin == 0




        