class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
            
        ans = 0
        fuel = 0
        for i in range(len(cost)):
            fuel += gas[i]
            fuel -= cost[i]
            if fuel<0:
                fuel=0
                ans=i+1
            
        return ans
        