class Solution:
    def longestPalindrome(self, s: str) -> str:
        pipedS = "|".join([c for c in s])
        pipedS = "|"+pipedS+"|"
        P = [0]*len(pipedS)
        C,R = 0,0
        m = 0
        n = 0 # The walking indices to compare if two elements are the same.
        for i,c in enumerate(pipedS): 
            if i > R:
                P[i] = 0
                m = i-1
                n = i+1;
            else:
                i2 = C*2-i;
                if P[i2]<(R-i-1):
                    P[i] = P[i2]
                    m = -1 # This signals bypassing the while loop below. 
                else:
                    P[i] = R-i
                    n = R+1
                    m = i*2-n
            while m>=0 and n<len(pipedS) and pipedS[m]==pipedS[n]:
                P[i]+=1
                m-=1
                n+=1
            if i+P[i]>R:
                C = i
                R = i+P[i]
        l = 0
        C = 0
        for i in range(len(pipedS)):
            if l<P[i]:
                l = P[i]
                C = i
        return "".join([c for c in pipedS[C-l:C+l+1] if c!= "|"])