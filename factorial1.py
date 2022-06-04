# factorial iterative
# def fact(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i+1)
#     return fact


# print(fact(5))

# time complexity = o(n)

# factorial recursive
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(5))
# time complexity = o(n)
