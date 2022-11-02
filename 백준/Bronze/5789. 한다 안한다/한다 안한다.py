from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        table: str = stdin.readline().rstrip()
        isDo: bool = False
        while len(table) > 1:
            if table[0] == table[-1]:
                isDo = True
            else:
                isDo = False
            table = table[1:-1]

        stdout.write("Do-it\n" if isDo else "Do-it-Not\n")


if __name__ == "__main__":
    solution()