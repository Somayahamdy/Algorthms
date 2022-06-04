#  buble_sort recursive
# def bubbleSort(arr):
#     n = len(arr)


#     for i in range(n):

#
#         for j in range(0, n-i-1):

#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


#
# arr = [64, 34, 25, 12, 22, 11, 90]

# bubbleSort(arr)

# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])

# time complexity = o(n^2)
####################################################################
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array :")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")


# time complexity = o(n^2)
