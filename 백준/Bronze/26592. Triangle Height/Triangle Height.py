from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        area, base = (map(float, stdin.readline().rstrip().split()))
        stdout.write("The height of the triangle is %.2f units\n" % (round(area / base * 2, 2)))


if __name__ == "__main__":
    solution()
