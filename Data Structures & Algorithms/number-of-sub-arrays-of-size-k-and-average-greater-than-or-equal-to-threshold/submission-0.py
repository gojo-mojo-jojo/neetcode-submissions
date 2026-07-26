class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        #lut = set()
        L = 0
        count = 0
        sum  = 0
        avg = 0
        for R in range(len(arr)):
            sum += arr[R]
            if R - L + 1 >= k :
                avg = sum/k
                if avg >= threshold:
                    count+=1
                sum -= arr[L] 
                L += 1
           
            
           # lut.add(arr[R])
        
        return count



        