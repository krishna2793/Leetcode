class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        kHeap = []
        for point in points:
            d = point[0]**2 + point[1]**2
            heapq.heappush(kHeap,(-d,point))
            if len(kHeap)>K:
                heapq.heappop(kHeap)
        return [item[1] for item in kHeap]