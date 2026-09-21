num = int(input("Enter a number: "))

digits =0
count = 0
while num > 0:
    digit = num % 10
    count = count * 10 + digit
    num = num // 10

print("Reversed digits:", count)