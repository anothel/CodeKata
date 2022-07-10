from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        stdout.write("%s\n" % stdin.readline().rstrip().lower())


if __name__ == "__main__":
    solution()
