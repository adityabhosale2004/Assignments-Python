import sys

X = input("Enter the number: ")

print(X)
print("Data type : ",type(X))
print("Memory Address is : ",id(X))
print("Size of Vaiable in bytes :",sys.getsizeof(X))
