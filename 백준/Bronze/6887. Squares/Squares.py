from sys import stdin, stdout


def solution():
    n = int(stdin.readline().rstrip())

    stdout.write("The largest square has side length %d.\n" % n**0.5)


if __name__ == "__main__":
    solution()
