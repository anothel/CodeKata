from sys import stdin, stdout


def solution():
    cow: list = [-1] * 10
    n: int = int(stdin.readline().rstrip())
    answer: int = 0
    for _ in range(n):
        a, b = map(int, stdin.readline().rstrip().split())
        a -= 1
        if cow[a] == -1:
            cow[a] = b
        elif cow[a] != b:
            cow[a] = b
            answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
