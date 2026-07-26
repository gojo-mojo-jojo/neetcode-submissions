import heapq
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        gas_stations = len(gas)

        new_gas = [ (-amount, i) for i, amount in enumerate(gas)]
        heapq.heapify(new_gas)

        while new_gas:
            _, start_index = heapq.heappop(new_gas)
            
            spent = 0
            total_tank = 0
            for i in range(start_index, gas_stations+start_index):
                j = i
                i = i%gas_stations
                
                total_tank += gas[i]

                #Go to Next Station
                spent = cost[i]
                total_tank  = total_tank -  spent

                if total_tank < 0: #cant reach next station
                    break #choose next max

                if j + 1 == gas_stations+start_index:
                    return start_index
                    


        return -1
