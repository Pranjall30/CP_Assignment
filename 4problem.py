def modulo(a, b, m):
    return (a ** b) % m

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
m = int(input("Enter the value of m: "))

result = modulo(a, b, m)
print("Result: ", result)