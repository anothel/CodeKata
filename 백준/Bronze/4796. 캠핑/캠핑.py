from sys import stdin, stdout


def solution():
    i: int = 1
    while True:
        l, p, v = map(int, stdin.readline().rstrip().split())
        if l + p + v == 0:
            break

        answer: int = 0
        answer += (v // p) * l
        answer += v - ((v // p) * p) if v - ((v // p) * p) < l else l

        stdout.write("Case %d: %d\n" % (i, answer))
        i += 1


if __name__ == "__main__":
    solution()
