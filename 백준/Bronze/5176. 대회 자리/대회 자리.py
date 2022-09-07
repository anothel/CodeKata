from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        p, m = map(int, stdin.readline().rstrip().split())
        seats: list = [0 for _ in range(m)]
        answer: int = 0
        for _ in range(p):
            num: int = int(stdin.readline().rstrip())
            if seats[num - 1] == 0:
                seats[num - 1] = 1
            else:
                answer += 1
        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
