src = "data/liczby.txt"
# src = "data/przyklad.txt"

with open(src, "r", encoding="utf-8") as file:
    counter = 0
    firstTargetNumber = ""

    for line in file.readlines():
        line = line.strip()
        firstChar = line[0]
        lastChar = line[-1]

        if firstChar == lastChar:
            counter += 1

            if counter == 1:
                firstTargetNumber = line

    print(counter, firstTargetNumber)

