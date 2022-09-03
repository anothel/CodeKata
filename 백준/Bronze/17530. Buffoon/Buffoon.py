from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    score: int = int(stdin.readline().rstrip())

    for _ in range(n - 1):
        if int(stdin.readline().rstrip()) > score:
            stdout.write("N\n")
            return
    stdout.write("S\n")


if __name__ == "__main__":
    solution()
