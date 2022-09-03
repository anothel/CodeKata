from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        answer: int = 0
        n, m = map(int, stdin.readline().rstrip().split())

        for i in range(n, m + 1):
            answer += str(i).count('0')

        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
