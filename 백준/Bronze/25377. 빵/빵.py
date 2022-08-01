from sys import stdin, stdout


def solution():
    answer: int = 1001
    for _ in range(int(stdin.readline().rstrip())):
        a, b = map(int, stdin.readline().rstrip().split())
        if a <= b and b < answer:
            answer = b
    stdout.write("%d\n" % answer if answer != 1001 else "-1\n")


if __name__ == "__main__":
    solution()
