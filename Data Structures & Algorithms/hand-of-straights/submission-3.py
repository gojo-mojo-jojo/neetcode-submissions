from _heapq import heapify
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        lut = {}
        for n in hand:
            lut[n] = lut.get(n, 0) + 1
        
        min_heap = list(lut.keys())
        heapq.heapify(min_heap)

        while len(min_heap):
            val = min_heap[0]
            for i in range(val, val+groupSize):
                if i not in lut:
                    return False
                lut[i] -= 1
                if lut[i] == 0:
                    heapq.heappop(min_heap)
        return True
