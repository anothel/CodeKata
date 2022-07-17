from sys import stdin, stdout


def solve():
    n, k = map(int, stdin.readline().rstrip().split())
    answer: list = list()

    for i in range(1, n + 1):
        if i % 10 != k % 10 and i % 10 != (2 * k) % 10:
            answer.append(i)
    stdout.write("%d\n" % len(answer))
    for i in answer:
        stdout.write("%d " % i)


if __name__ == "__main__":
    solve()
