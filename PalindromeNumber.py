class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        temp = x
        while temp:
            rev *=10
            rev+=temp%10
            temp = math.floor(temp/10)
        return rev==x