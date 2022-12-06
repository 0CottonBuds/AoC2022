def getCommonItem(elves: list):
    duplicates = [char for char in elves[0] if char in elves[1] and char in elves[2]]
    return duplicates[0]


from part1 import getPriority

if __name__ == "__main__":
    # get input
    input = open("input.txt", "r").read()
    input = input.split("\n")

    elves = []
    # unpack the rucksacks
    for elf in input:
        elves.append([*elf])

    groupOfElves = []
    # group the elves to the group of 3
    for i in range(0, len(elves), 3):
        groupOfElves.append(elves[i : i + 3])

    duplicates = []
    for elves in groupOfElves:
        duplicates.append(getCommonItem(elves))

    sum = 0
    for duplicate in duplicates:
        sum += getPriority(duplicate)

    print(sum)
