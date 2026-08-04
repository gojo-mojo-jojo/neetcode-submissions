class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(i, total, curr_list):

            if total == target:
                res.append(curr_list.copy())
                return 

            if i >= len(candidates) or total > target:
                return

            # curr_list.append(candidates[i])
            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j-1]:
                    continue
                num = candidates[j]
                curr_list.append(num)
                dfs(j+1, total + num, curr_list)
                curr_list.pop()

            return
        
        dfs(0, 0, [])
        return res
        