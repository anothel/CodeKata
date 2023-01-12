from sys import stdin, stdout


def solution():
    s: list = (stdin.readline().rstrip())

    cur: int = 0

    while cur < len(s):
        stdout.write("%s" % s[cur])
        cur += (ord(s[cur]) - 64)


if __name__ == "__main__":
    solution()
