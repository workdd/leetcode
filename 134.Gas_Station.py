class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_station = 0
        total = 0
        tank = 0

        for i in range(len(gas)):
            remain = gas[i] - cost[i]
            total += remain

            tank += remain
            if tank < 0:
                start_station = i + 1
                tank = 0

        if total < 0:
            return -1
        else:
            return start_station
