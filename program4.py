#Write a function to accept two numbers and return their multiplication

def multiply(No1,No2):
    result = No1 * No2
    return result

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

Ans = multiply(x, y)
print("Multiplication is:", Ans)
