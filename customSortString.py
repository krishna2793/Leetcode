class Solution:
    def customSortString(self, S: str, T: str) -> str:
        itr = 0
        left = ""
        right = ""
        Temp = T
        for i,c in enumerate(S):
            index = Temp.find(c)
            while index >= 0:
                left += c
                Temp = Temp[0:index] + Temp[index+1:len(Temp)]
                index = Temp.find(c)
        return left+Temp