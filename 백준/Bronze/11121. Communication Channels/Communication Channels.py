from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        n, m = map(str, stdin.readline().rstrip().split())
        stdout.write("ERROR\n" if n != m else "OK\n")


if __name__ == "__main__":
    solution()
