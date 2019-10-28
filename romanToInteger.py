class Solution:
    def romanToInt(self, s: str) -> int:
        l = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        i = 0
        n = len(s)
        tot = 0
        while i<n:
            if (i+1)<n:
                if l[s[i]]<l[s[i+1]]:
                    tot-=l[s[i]]
                    i+=1
            tot+=l[s[i]]
            i+=1
        return tot