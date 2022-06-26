from sys import stdin, stdout


def solution():
    x: int = int(stdin.readline().rstrip())
    for _ in range(int(stdin.readline().rstrip())):
        a, b = map(int, stdin.readline().rstrip().split())
        x -= a * b
    stdout.write("Yes\n" if x == 0 else "No\n")


if __name__ == "__main__":
    solution()
