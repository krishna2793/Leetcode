class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxFruits = 0
        second = tree[0]
        start = 0
        currRepeat = 0
        for i in range(1,len(tree)):
            if tree[i-1] != tree[i]:
                if second == tree[currRepeat]:
                    second = tree[currRepeat]
                    currRepeat = i
                elif tree[i] == second:
                    second = tree[i-1]
                    currRepeat = i
                else:
                    maxFruits = max(maxFruits,i-start)
                    start = currRepeat
                    second = tree[currRepeat]
                    currRepeat = i
        maxFruits = max(maxFruits,len(tree)-start)
        return maxFruits