class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv", "wxyz"]
        ret = []
        
        for digit in digits:
            dRet = []
            for s in ret:
                for c in numMap[int(digit)]:
                    dRet.append(s+c)
            ret = dRet
            if len(ret) ==0:
                for c in numMap[int(digit)]:
                    dRet.append(""+c)
        return ret