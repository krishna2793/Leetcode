class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        interval = {}
        ret = []
        for i,c in enumerate(S):
            if c in interval:
                interval[c] = (interval[c][0],i)
            else:
                interval[c] = (i,i)
        interval = sorted(interval.values())
        (start,end) = interval[0]
        for item in interval[1:]:
            if item[0]>end:
                ret.append(end+1-start)
                (start,end) = item
            else:
                end = max(end,item[1])
        ret.append(end+1-start)
        return ret