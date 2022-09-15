from sys import stdin, stdout


def solution():
    n, k, l = map(int, stdin.readline().rstrip().split())
    answer: list = list()
    for i in range(n):
        x1, x2, x3 = map(int, stdin.readline().rstrip().split())
        if x1 < l or x2 < l or x3 < l or (x1 + x2 + x3) < k:
            continue
        answer.append(x1)
        answer.append(x2)
        answer.append(x3)
    stdout.write("%d\n" % (len(answer) // 3))
    for i in answer:
        stdout.write("%d " % i)


if __name__ == "__main__":
    solution()