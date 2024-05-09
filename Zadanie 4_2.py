def prime_factors(n):
    result = []

    factor = 2
    while True:

        if n % factor == 0:
            result.append(factor)
            n //= factor
        else:
            factor += 1

        if n == 1:
            break

    return result

# print(prime_factors(420))
# print(list(set(prime_factors(420))))

src = "data/liczby.txt"
# src = "data/przyklad.txt"

with open(src, "r", encoding="utf-8") as file:

    mostFactorsNumber = 0
    mostFactorValue = 0

    mostUniqueFactorsNumber = 0
    mostUniqueFactorValue = 0

    for line in file.readlines():
        line = line.strip()

        factorList = prime_factors(int(line))
        uniqueFactorList = list(set(factorList))

        if len(factorList) > mostFactorValue:
            mostFactorValue = len(factorList)
            mostFactorsNumber = int(line)

        if len(uniqueFactorList) > mostUniqueFactorValue:
            mostUniqueFactorValue = len(uniqueFactorList)
            mostUniqueFactorsNumber = int(line)


    print(mostFactorsNumber, mostFactorValue, mostUniqueFactorsNumber, mostUniqueFactorValue)



