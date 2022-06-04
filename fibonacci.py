# fibonacci recursive

# calculate = 9


# def fibonacci(number):
#     if number <= 1:
#         return number
#     else:
#         return(fibonacci(number-1) + fibonacci(number-2))


# for number in range(calculate):
#     print(fibonacci(number))

# time complexity = o(n)


# fibonacci iterative
terms_to_calculate = 4
num1, num2 = 0, 1
counter = 0
while counter < terms_to_calculate:
    print(num1)
    new_number = num1 + num2
    num1 = num2
    num2 = new_number
    counter += 1

# time complexity = o(n)
