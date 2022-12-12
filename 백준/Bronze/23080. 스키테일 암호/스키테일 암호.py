from sys import stdin, stdout


def solution():
    k: int = int(stdin.readline().rstrip())
    s: list = list(stdin.readline().rstrip())

    for i in range(len(s)):
        if i % k == 0:
            stdout.write("%s" % s[i])


if __name__ == "__main__":
    solution()
