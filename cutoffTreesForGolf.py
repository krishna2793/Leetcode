from operator import itemgetter
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def neighbor(forest,R,C,y,x):
            for i,j in zip([0,0,-1,1],[-1,1,0,0]):
                if (y+i)<R and (y+i)>=0 and (x+j)<C and (x+j)>=0 and forest[y+i][x+j]>0:
                    yield y+i,x+j
        def countSteps(start, end, forest, R,C):
            if forest[start[0]][start[1]]==0:
                return -1
            elif start == end:
                forest[start[0]][start[1]]=1
                return 0
            else:
                count = 0
                minSteps = -1
                temp = forest[start[0]][start[1]]
                forest[start[0]][start[1]] = 0
                for n in neighbor(forest,R,C,start[0],start[1]):
                    steps = countSteps(n,end,forest,R,C)
                    if steps>=0 and minSteps<steps:
                        minSteps = steps
                forest[start[0]][start[1]] = temp
                if minSteps >=0:
                    return minSteps+1
                else:
                    return -1
        def hadlocks(sr, sc, tr, tc, forest, R, C):
            processed = set()
            deque = collections.deque([(0, sr, sc)])
            while deque:
                detours, r, c = deque.popleft()
                if (r, c) not in processed:
                    processed.add((r, c))
                    if r == tr and c == tc:
                        forest[r][c] = 1
                        return abs(sr-tr) + abs(sc-tc) + 2*detours
                    for nr, nc, closer in ((r-1, c, r > tr), (r+1, c, r < tr),
                                           (r, c-1, c > tc), (r, c+1, c < tc)):
                        if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                            if closer:
                                deque.appendleft((detours, nr, nc))
                            else:
                                deque.append((detours+1, nr, nc))
            return -1
        R = len(forest)
        C = len(forest[0])
        trees = [(i,j,forest[i][j]) for i in range(R) for j in range(C) if forest[i][j]>1]
        trees = sorted(trees, key=itemgetter(2))
        start = (0,0)
        steps = 0
        for end in trees:
            #print(start,end,forest)
            count = hadlocks(start[0], start[1], end[0], end[1], forest, R,C)
            if count <0:
                return -1
            else:
                steps+=count
                start = (end[0],end[1])
        return steps