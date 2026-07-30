class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        

        while len(max_heap) > 1:
            stone1 = -1*heapq.heappop(max_heap)
            stone2 = -1*heapq.heappop(max_heap)

            if stone1 > stone2:
                stone_x = stone1 - stone2
                heapq.heappush(max_heap, -stone_x)


        return abs(max_heap[0]) if len(max_heap) == 1 else 0