class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr_idx = 0
        curr_cost = 0
        if len(cost) == 3:
            if cost[0] + cost[2] < cost[1]:
                return cost[0] + cost[2]
            else:
                return cost[1]
        if len(cost) >= 2:
            if cost[0] < cost[1]:
                curr_cost += cost[0]
            else:
                curr_cost += cost[1]
                curr_idx = 1
        while curr_idx < (len(cost) - 2):
            if cost[curr_idx+1] < cost[curr_idx+2]:
                curr_cost += cost[curr_idx+1]
                curr_idx+=1
            else:
                curr_cost += cost[curr_idx+2]
                curr_idx+=2
        return curr_cost