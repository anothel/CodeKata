from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        a1, p1 = map(int, stdin.readline().rstrip().split())
        r1, p2 = map(int, stdin.readline().rstrip().split())
        area: float = 3.14 * r1 * r1

        if a1 / p1 < area / p2:
            stdout.write("Whole pizza\n")
        else:
            stdout.write("Slice of pizza\n")


if __name__ == "__main__":
    solution()
