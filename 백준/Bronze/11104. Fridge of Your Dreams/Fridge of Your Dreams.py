from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        binary: str = stdin.readline().rstrip()
        stdout.write("%d\n" % int(binary, 2))


if __name__ == "__main__":
    solution()
