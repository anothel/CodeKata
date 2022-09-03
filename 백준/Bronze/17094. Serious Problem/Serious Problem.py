from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    sen: str = stdin.readline().rstrip()

    c2: int = 0
    ce: int = 0

    for i in sen:
        if i == '2':
            c2 += 1
        elif i == 'e':
            ce += 1

    if c2 > ce:
        stdout.write("2\n")
    elif ce > c2:
        stdout.write("e\n")
    else:
        stdout.write("yee\n")


if __name__ == "__main__":
    solution()
