def getCommonMember(compartments: list):
    duplicates = [char for char in compartments[0] if char in compartments[1]]
    return duplicates[0]


def getPriority(char: str):
    unicode = ord(char[0])

    if 64 < unicode < 91:  # capital letter
        return unicode - 38
    elif 96 < unicode < 123:  # lower case letter
        return unicode - 96


if __name__ == "__main__":
    # get input
    input = open("input.txt", "r").read()
    rucksacks = input.split("\n")

    compartments = []

    duplicates = []
    # split the two compartments
    for rucksack in rucksacks:
        comp1, comp2 = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
        compartment1 = [*comp1]
        compartment2 = [*comp2]
        compartments.append([compartment1, compartment2])

    sumOfPriority = 0
    # check the duplicates in each compartment
    # check their priority
    for compartment in compartments:
        duplicate = getCommonMember(compartment)
        sumOfPriority += getPriority(duplicate)
        duplicates.append(duplicate)

    print(duplicates)
    print()
    print(sumOfPriority)
    # add to the sum
