src = "data/liczby.txt"
# src = "data/przyklad.txt"

with open(src, "r", encoding="utf-8") as file:
    with open("trojki.txt", "w", encoding="utf-8") as fileWithResult:
        counter = 0

        listOfNumbers = sorted([int(line.strip()) for line in file.readlines()])

        for i in range(len(listOfNumbers) - 2):
            for j in range(i + 1, len(listOfNumbers) - 1):
                for k in range(j + 1, len(listOfNumbers)):

                    number1 = listOfNumbers[i]
                    number2 = listOfNumbers[j]
                    number3 = listOfNumbers[k]

                    triple = [number1, number2, number3]

                    if triple[1] % triple[0] == 0 and triple[2] % triple[1] == 0:
                        counter += 1
                        fileWithResult.write(f"{triple[0]} {triple[1]} {triple[2]}\n")

        print(counter)
        secondCounter = 0

        for i in range(len(listOfNumbers) - 4):
            for j in range(i + 1, len(listOfNumbers) - 3):
                if listOfNumbers[j] % listOfNumbers[i] == 0:
                    for k in range(j + 1, len(listOfNumbers) - 2):
                        if listOfNumbers[k] % listOfNumbers[j] == 0:
                            for l in range(k + 1, len(listOfNumbers) - 1):
                                for m in range(l + 1, len(listOfNumbers)):

                                    number1 = listOfNumbers[i]
                                    number2 = listOfNumbers[j]
                                    number3 = listOfNumbers[k]
                                    number4 = listOfNumbers[l]
                                    number5 = listOfNumbers[m]

                                    pentaList = [number1, number2, number3, number4, number5]

                                    if pentaList[3] % pentaList[2] == 0 and pentaList[4] % pentaList[3] == 0:
                                        secondCounter += 1

        print(secondCounter)

