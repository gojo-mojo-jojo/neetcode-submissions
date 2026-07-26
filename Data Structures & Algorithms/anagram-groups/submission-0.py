class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in lookup:
                lookup[key] = []
            
            lookup[key].append(word)
        
        #return list(lookup.values())
        return [value for _,value in lookup.items()]

        