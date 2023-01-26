from sys import stdin, stdout


def solution():
    n, k, a, b = map(int, stdin.readline().rstrip().split())

    m = n * k
    p = a * b

    if m > p:
        stdout.write("M\n")
    elif p > m:
        stdout.write("P\n")
    else:
        stdout.write("E\n")


if __name__ == "__main__":
    solution()
