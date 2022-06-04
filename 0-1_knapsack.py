# optimal_solution
# def knapSack(W, wt, val, n):

#     if n == 0 or W == 0:
#         return 0

#     if (wt[n-1] > W):
#         return knapSack(W, wt, val, n-1)

#     else:
#         return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
#                    knapSack(W, wt, val, n-1))


# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print(knapSack(W, wt, val, n))

# greedy_knapsack_solution
def greedy_knapsack(values, weights, capacity):
    n = len(values)
    def score(i): return values[i]/weights[i]
    items = sorted(range(n), key=score, reverse=True)
    sel, value, weight = [], 0, 0
    for i in items:
        if weight + weights[i] <= capacity:
            sel += [i]
            weight += weights[i]
            value += values[i]
    return sel, value, weight


weights = [4, 9, 10, 20, 2, 1]
values = [400, 1800, 3500, 4000, 1000, 200]
capacity = 20

print(greedy_knapsack(values, weights, capacity))
