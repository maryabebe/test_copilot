def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

num = int(input("Enter an integer: "))
print("The factors of", num, "are:", find_factors(num))