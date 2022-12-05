def checkIfWinOrLose(game: list[str]) -> int:
    yourMove = game[1]
    opponentsMove = game[0]

    score = 0

    if yourMove == "X":  # you picked rock
        if opponentsMove == "B":  # if opponent picked paper
            # lost
            score += 0 + 1
        elif opponentsMove == "C":  # if opponent picked scissors
            # win
            score += 6 + 1
        elif opponentsMove == "A":
            # draw
            score += 3 + 1
        else:
            pass
    elif yourMove == "Y":  # you picked paper
        if opponentsMove == "C":  # opponent picked scissors
            # lost
            score += 0 + 2
        elif opponentsMove == "A":  # opponent picked rock
            # win
            score += 6 + 2
        elif opponentsMove == "B":
            # draw
            score += 3 + 2
        else:
            pass
    elif yourMove == "Z":  # picked scissors
        if opponentsMove == "A":  # picked rock
            # lost
            score += 0 + 3
        elif opponentsMove == "B":  # picked paper
            # win
            score += 6 + 3
        elif opponentsMove == "C":
            # draw
            score += 3 + 3
        else:
            pass
    return score


def getScoreIfFollowedPlan(game: list[str]):
    opponentsMove = game[0]
    choice = game[1]

    winningChoices = [["A", "Y"], ["B", "Z"], ["C", "X"]]
    losingChoices = [["A", "Z"], ["B", "X"], ["C", "Y"]]
    drawChoices = [["A", "X"], ["B", "Y"], ["C", "Z"]]

    if choice == "Z":  # if you need to win
        if opponentsMove == "A":
            return winningChoices[0]
        elif opponentsMove == "B":
            return winningChoices[1]
        elif opponentsMove == "C":
            return winningChoices[2]
        else:
            print("bug")
    elif choice == "Y":  # if you need to draw
        if opponentsMove == "A":
            return drawChoices[0]
        elif opponentsMove == "B":
            return drawChoices[1]
        elif opponentsMove == "C":
            return drawChoices[2]
        else:
            print("bug")
    elif choice == "X":  # if you need to lose
        if opponentsMove == "A":
            return losingChoices[0]
        elif opponentsMove == "B":
            return losingChoices[1]
        elif opponentsMove == "C":
            return losingChoices[2]
        else:
            print("bug")
    else:
        print("bug")


if __name__ == "__main__":
    input = open("input.txt", "r")
    games = input.read()
    games = games.split("\n")
    games = [game.split(" ") for game in games]

    totalScore = 0
    for game in games:
        choice = getScoreIfFollowedPlan(game)
        totalScore += checkIfWinOrLose(choice)
    print(totalScore)
