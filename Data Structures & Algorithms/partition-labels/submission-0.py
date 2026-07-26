class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        #create hash map: char: start, last
        hashset = {}
        for i, char in enumerate(s):
            
            if char not in hashset:
                hashset[char] = (i,i)
            else:
                hashset[char] = (hashset[char][0], i)

        
        output = []

        partition = 0
        curr_last = 0
        length = 0
        for i in range(len(s)):
            last_index = hashset[s[i]][1]
            curr_last = max(curr_last, last_index)
            #partition =  max(partition, curr_last-i+1)
            length += 1
            if i == curr_last:
                output.append(length)
                length = 0
                curr_last = 0

        return output








        