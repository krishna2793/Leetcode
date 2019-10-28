class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        factMem = [1]
        def fact(n):
            if n>=len(factMem):
                for i in range(len(factMem),n+1):
                    factMem.append(i*factMem[i-1])
            return factMem[n]
        def nPr(n,r):
            return (int(fact(n)/fact(n-r)))
        def Poss(n,freq):
            poss = 0
            for key in freq.keys():
                if freq[key]>0:
                    freq[key] -= 1
                    poss+=Poss(n-1, freq)
                    freq[key] += 1
            return poss+1
        freq = collections.defaultdict(int)
        for c in tiles:
            freq[c]+=1
        return Poss(len(tiles), freq)-1