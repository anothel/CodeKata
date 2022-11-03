from sys import stdin, stdout


def solution():
    stdout.write("%s\n" % bin(int(stdin.readline().rstrip()))[2:])


if __name__ == "__main__":
    solution()