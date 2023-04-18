from sys import stdin, stdout


def solution():

    n, m = map(int, stdin.readline().strip().split())
    if n * 100 >= m:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solution()
