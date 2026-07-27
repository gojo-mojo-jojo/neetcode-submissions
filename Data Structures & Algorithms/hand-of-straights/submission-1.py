from _heapq import heapify
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        if len(hand) % groupSize > 0:
            return False


        hashset = {}

        for num in hand:
            hashset[num] = hashset.get(num, 0) + 1

        
        hand.sort()
        #[1,2,4,2,3,5,3,4] --> [1,1,2,3,3,4,4,5] [1,2,3,4,5]
        min_heap = [k for k in hashset.keys()]
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            #prev =  start
            for j in range(start, start + groupSize):
                # if prev != j and hashset[j] <= 0:
                #     return False
                if j not in hashset:
                    return False

                hashset[j] -= 1

                if hashset[j] == 0:
                    if j != min_heap[0]: #that means its lesser value isnt still popped
                        return False
                    heapq.heappop(min_heap)
                #prev = j
        return True



