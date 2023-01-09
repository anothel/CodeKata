from sys import stdin, stdout


def solution():
    c: list = list(map(str, stdin.readline().rstrip().split()))

    stdout.write("YES\n" if int(c[0]) + int(c[2]) == int(c[4]) else "NO\n")


if __name__ == "__main__":
    solution()
