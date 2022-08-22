from sys import stdin, stdout


def solution():
    n, l, k = map(int, stdin.readline().rstrip().split())

    answer: int = 0
    sub1Count: int = 0
    sub2Count: int = 0

    for _ in range(n):
        sub1, sub2 = map(int, stdin.readline().rstrip().split())

        if sub1Count + sub2Count < k:
            if sub2 <= l:
                answer += 140
                sub2Count += 1
            elif sub1 <= l:
                answer += 100
                sub1Count += 1
        else:
            if 0 < k and sub1Count + sub2Count == k and 0 < sub1Count and sub2 <= l:
                answer += 40
                sub2Count += 1
                sub1Count -= 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
