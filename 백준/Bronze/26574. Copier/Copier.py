from sys import stdin, stdout


def solution():

    n: int = int(stdin.readline().strip())
    for _ in range(n):
        t: int = int(stdin.readline().strip())
        print('{0} {1}'.format(t, t))


if __name__ == "__main__":
    solution()
