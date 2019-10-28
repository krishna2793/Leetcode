class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s,op,cl,n,ret):
            if cl == n:
                ret.add(s)
                return
            if cl<op:
                backtrack(s+")",op,cl+1,n,ret)
            if op<n:
                backtrack(s+"(",op+1,cl,n,ret)
        ret = set()
        backtrack("",0,0,n,ret)
        return list(ret)