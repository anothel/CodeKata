from sys import stdin, stdout


def solution():
    n, m = map(int, stdin.readline().rstrip().split())

    dogam: list = list()

    for _ in range(n):
        dogam.append(stdin.readline().rstrip())

    for _ in range(m):
        insert: str = stdin.readline().rstrip()

        if insert.isdigit():
            stdout.write("%s\n" % dogam[int(insert) - 1])
        else:
            stdout.write("%s\n" % (dogam.index(insert) + 1))


if __name__ == "__main__":
    solution()
