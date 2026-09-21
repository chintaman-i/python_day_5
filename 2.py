num = int(input("Enter a number: "))
length = 0

while num > 0:
    length += 1
    num = num // 10

print(length)