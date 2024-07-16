class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        if (sum(gas)<sum(cost)):
            return -1
        totTank,currTank = 0,0
        start = 0
        for i in range(n):
            totTank += gas[i] - cost[i]
            currTank += gas[i] - cost[i]
            if (currTank<0):
                start = i+1
                currTank = 0
        return start if totTank>=0 else -1
            
