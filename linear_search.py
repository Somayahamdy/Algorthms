# linear_search iteritve
# list_of_elements = [4, 2, 8, 9, 3, 7]
# x = int(input("Enter number to search: "))

# found = False

# for i in range(len(list_of_elements)):
#     if(list_of_elements[i] == x):
#         found = True
#         print("%d found at %dth position" % (x, i))
#         break

# if(found == False):
#     print("%d is not in list" % x)


# time complexity = o(n)

# linear_search recursive
def search(ls, key, idx=0):

    if ls:
        if ls[0] == key:
            return idx

    s = search(ls[1:], key, (idx + 1))
    if s is not False:
        return s

    return False


list = [4, 2, 8, 9, 3, 7]

print(search(list, 4, idx=0))

# time complexity = o(n)
