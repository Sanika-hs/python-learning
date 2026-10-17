number = 7

a = 0
b = 1

print("Enter the number of terms:", number)
print("Fibonacci series:")

for i in range(number):
    print(a, end=" ")
    a, b = b, a + b

print()