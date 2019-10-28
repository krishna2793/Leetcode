class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def rec(str1,str2):
            if len(str2) == 0:
                return str1
            elif len(str1)<len(str2):
                return rec(str2,str1)
            if str2 not in str1:
                return ""
            else:
                return rec(str2,str1[len(str2):])
        return rec(str1,str2)