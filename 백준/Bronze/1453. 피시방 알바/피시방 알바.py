from sys import stdin, stdout


def solution():
    n = int(stdin.readline().rstrip())
    custom: list = list(map(int, stdin.readline().rstrip().split()))
    count: int = 0
    seat: list = list()
    for i in range(n):
        if custom[i] in seat:
            count += 1
        else:
            seat.append(custom[i])
    stdout.write("%d\n" % count)


if __name__ == "__main__":
    solution()