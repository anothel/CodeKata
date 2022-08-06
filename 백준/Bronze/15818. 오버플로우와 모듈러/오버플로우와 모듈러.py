from sys import stdin, stdout


def solution():
    n, m = map(int, stdin.readline().rstrip().split())
    if n == 1:
        stdout.write("%d\n" % (int(stdin.readline().rstrip()) % m))
    else:
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        answer: int = 1
        for i in nums:
            answer *= i
        stdout.write("%d\n" % (answer % m))


if __name__ == "__main__":
    solution()
