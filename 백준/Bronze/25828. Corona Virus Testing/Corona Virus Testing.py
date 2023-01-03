from sys import stdin, stdout


def solution():
    g, p, t = map(float, stdin.readline().rstrip().split())

    e: int = g * p
    o: int = g + t * p

    if e < o:
        stdout.write("1\n")
    elif o < e:
        stdout.write("2\n")
    else:
        stdout.write("0\n")


if __name__ == "__main__":
    solution()
