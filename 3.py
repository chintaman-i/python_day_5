num = int(input("Enter a number: "))

digits = []

while num > 0:
    digit = num % 10
    digits.append(digit)
    num = num // 10

print("Reversed digits:", digits)