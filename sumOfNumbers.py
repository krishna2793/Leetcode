class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def atoi(c):
            return (ord(c)-ord('0'))
        n1 = len(num1)
        n2 = len(num2)
        rem = 0
        ret = ""
        for i in range(max(n1,n2)):
            #print(ret)
            add = rem
            if (n1-i-1) >=0 and (n1-i-1)<n1:
                add+=atoi(num1[n1-i-1])
            if (n2-i-1) >=0 and (n2-i-1)<n2:
                add+=atoi(num2[n2-i-1])
            if add>9:
                rem = 1
            else:
                rem = 0
            ret = str(add%10) + ret
        if rem>0:
            ret = str(rem) + ret
        return ret