from sys import stdin, stdout


def solution():
    a: int = int(stdin.readline().rstrip())
    b: int = int(stdin.readline().rstrip())

    if a + b * 7 > 30:
        stdout.write("0\n")
    else:
        stdout.write("1\n")


if __name__ == "__main__":
    solution()
