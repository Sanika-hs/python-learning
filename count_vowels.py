text = input("Enter a word: ")

count = 0

for letter in text.lower():
    if letter in "aeiou":
        count = count + 1

print(text)
print("Number of vowels:", count)