# Q1
import numpy as np
alphabet = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(alphabet.dtype)
print(np.shape(alphabet))
print(np.size(alphabet))  # print(alphabet.size())

# Q2
points = int(input("enter number of points \n"))

if(1 <= points <= 50):
    print("wooden rabbit")

elif(51 <= points <= 150):
    print("no prize")
elif(151 <= points <= 180):
    print("wafer_thin_mint")
elif(181 <= points <= 200):
    print("penguin")
# Q3
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))
# Q4
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
