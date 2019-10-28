class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sqr = [i*i for i in A]
        sqr.sort()
        return sqr