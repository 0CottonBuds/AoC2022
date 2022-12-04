input = open("data.txt", "r")
calories: str = input.read()
calories = calories.split("\n\n")
calories = [i.split("\n") for i in calories]

# convert string list to int list
cal = [list(map(int, groupOfCalorie)) for groupOfCalorie in calories]
# sum of calories of each elf
sumOfCalories = [sum(sumOfCalories) for sumOfCalories in cal]
# sort the list
sortedSumOfCalorie = sumOfCalories.sort(reverse=True)

# check the largest number
first = sumOfCalories[0]
second = sumOfCalories[1]
third = sumOfCalories[2]


print(sum((first, second, third)))
