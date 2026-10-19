number = int(input("Enter number: "))

original = number
total = 0
digits = len(str(number))

while number > 0:
    digit = number % 10
    total = total + digit ** digits
    number = number // 10

print(original)

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")