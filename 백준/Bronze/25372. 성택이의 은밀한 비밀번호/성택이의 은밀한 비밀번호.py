from sys import stdin, stdout


def solve():
    for _ in range(int(stdin.readline().rstrip())):
        nLength: int = len(stdin.readline().rstrip())
        if 6 <= nLength and nLength <= 9:
            stdout.write("yes\n")
            continue
        stdout.write("no\n")


if __name__ == "__main__":
    solve()
