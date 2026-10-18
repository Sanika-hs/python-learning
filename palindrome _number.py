number = int(input("Enter number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print()
print(original)

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")