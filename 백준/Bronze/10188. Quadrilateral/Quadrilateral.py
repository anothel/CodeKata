from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    for _ in range(n):
        a, b = map(int, stdin.readline().rstrip().split())
        for _ in range(b):
            for _ in range(a):
                stdout.write("X")
            stdout.write("\n")
        stdout.write("\n")


if __name__ == "__main__":
    solution()
