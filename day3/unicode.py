while True:
    letter = input()

    def getPriority(char: str):
        unicode = ord(char[0])

        if 64 < unicode < 91:  # capital letter
            return unicode - 38
        elif 96 < unicode < 123:  # lower case letter
            return unicode - 96

    print(getPriority(letter))
