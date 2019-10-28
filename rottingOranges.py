class Solution:
    def nearby(x,y,C,R):
        neighbors = List()
        for i in [-1,1]:
            for j in [-1,1]:
                point = (x+i,y+j)
                if not (point[0]<0 or point[1]<0 or point[0]>=C or point[1]>=R):
                    neighbors.append(point)
        return neighbors
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def nearby(x,y,C,R):
            neighbors = []
            for i,j in zip([0,0,-1,1],[-1,1,0,0]):
                point = (x+i,y+j)
                if not (point[0]<0 or point[1]<0 or point[0]>=C or point[1]>=R):
                    neighbors.append(point)
            return neighbors
        
        R = len(grid[0])
        C = len(grid)
        rotten = []
        for i in range(C):
            for j in range(R):
                if grid[i][j] == 2:
                    rotten.append((i,j,0)) 
        bfs = rotten
        maxD = 0;
        while len(bfs)!=0:
            itr = bfs.pop(0)
            neighbors = nearby(itr[0], itr[1], C, R)
            for (i,j) in neighbors:
                if grid[i][j] == 1:
                    bfs.append((i,j,itr[2]+1))
                    grid[i][j] = 2
                    maxD = max(maxD, itr[2]+1)
            print(grid)
        for i in range(C):
            for j in range(R):
                if grid[i][j] == 1:
                    return -1
            
        return maxD