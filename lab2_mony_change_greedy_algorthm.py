# greedy_solution
def mony_change(x):
    piece_of_mony = [200, 100, 50, 20, 10, 5, 1, 0.5]
    i = 0

    while(x > 0):
        if(piece_of_mony[i] > x):
            i = i+1
        else:
            print(str(piece_of_mony[i]))
            x -= piece_of_mony[i]


mony_change(67)
# time complexity O(x)


# optimal_solution
# maxsize = 10000000


# def coinChange(S, sum):

#     dp = [0] * (sum + 1)

#     for i in range(1, sum + 1):

#         dp[i] = maxsize

#         for c in range(len(S)):
#             if i - S[c] >= 0:
#                 result = dp[i - S[c]]

#                 if result != maxsize:
#                     dp[i] = min(dp[i], result + 1)

#     return dp[sum]


# piece_of_mony = [200, 100, 50, 20, 10, 5, 1]
# coinChange(piece_of_mony, 67)
