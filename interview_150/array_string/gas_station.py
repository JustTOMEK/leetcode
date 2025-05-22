class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        current_gas = 0
        current_start = 0
        number_of_stations = len(gas)
        for i in range(number_of_stations):
            current_gas += gas[i]
            current_gas -= cost[i]
            if current_gas < 0:
                current_gas = 0
                current_start = i + 1
        return current_start