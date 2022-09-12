from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        i, f = map(int, stdin.readline().rstrip().split())
        stdout.write("Yes\n" if (i <= 1 and f <= 2) or (
            i <= 2 and f <= 1) else "No\n")


if __name__ == "__main__":
    solution()
