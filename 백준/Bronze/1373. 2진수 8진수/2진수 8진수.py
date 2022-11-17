from sys import stdin, stdout


def solution():
    b: str = int(stdin.readline().rstrip(), 2)
    stdout.write("%s\n" % oct(b)[2:])


if __name__ == "__main__":
    solution()