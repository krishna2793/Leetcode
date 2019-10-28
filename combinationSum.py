class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(array, addend, index, path, result,N):
            if addend <0:
                return
            elif addend==0:
                result.append(path)
                return
            for i in range(index,N):
                backtrack(array, addend-array[i], i, path+[array[i]], result, N)
        candidates.sort()
        result = []
        backtrack(candidates,target,0,[],result,len(candidates))
        return result