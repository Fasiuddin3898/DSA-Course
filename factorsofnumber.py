number = int(input("Enter a number: "))
factors = []

for i in range(1, (number // 2) + 1):
    if number % i == 0:
        factors.append(i)
factors.append(number)

print(f"Factors of {number} are: {factors}")