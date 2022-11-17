from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        sen: list = list(map(str, stdin.readline().rstrip().split()))
        for i in sen:
            stdout.write("%s " % i[::-1])
        stdout.write("\n")


if __name__ == "__main__":
    solution()