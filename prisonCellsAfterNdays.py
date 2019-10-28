class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N > 14:
            N = N%14

        if N%14 == 0:
            N = 14
        
        for i in range(1, N+1):
            temp = [0]*len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    temp[i] = 1
                else:
                    temp[i] = 0
            cells = temp
        return(cells)