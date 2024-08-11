class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [0]*(len(cost)+1)
        min_cost = 0
        for i in range(2, len(cost)+1):
            costs[i] = min(cost[i-2]+cost[i-1]+costs[i-2]+costs[i-1],
            min(cost[i-2]+costs[i-2], cost[i-1]+costs[i-1]))
        return costs[-1]
