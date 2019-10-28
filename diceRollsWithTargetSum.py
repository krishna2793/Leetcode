class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        Mod = (10**9)+7
        mem = [[None for i in range(target+1)] for j in range(d+1)]
        for i in range(1,target+1):
            mem[1][i] = 1 if i<=f else 0
        #print(mem)
        def rec(dice,total):
            if total <= 0:
                return 0
            if mem[dice][total] is not None:
                return mem[dice][total]
            mem[dice][total] = sum(rec(dice-1,total-k) for k in range(1,f+1))%Mod
            
            #print(mem)
            return mem[dice][total]
        #print(mem)
        return rec(d,target)