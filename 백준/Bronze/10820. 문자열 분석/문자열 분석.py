from sys import stdin, stdout


def solution():
    while True:
        try:
            sen: str = stdin.readline().rstrip('\n')

            if not sen:
                break

            small: int = 0
            big: int = 0
            digit: int = 0
            space: int = 0
            for i in sen:
                if i.islower():
                    small += 1
                elif i.isupper():
                    big += 1
                elif i.isdigit():
                    digit += 1
                elif i.isspace():
                    space += 1

            stdout.write("%d %d %d %d\n" % (small, big, digit, space))
        except:
            break


if __name__ == "__main__":
    solution()