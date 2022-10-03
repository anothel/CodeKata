from sys import stdin, stdout


def solution():
    x, y = map(int, stdin.readline().rstrip().split())

    a: int = 100 - x
    b: int = 100 - y
    c: int = 100 - (a + b)
    d: int = a * b
    q: int = d // 100
    r: int = d % 100

    answer1: int = 0
    if d < 100:
        answer1 = c
    else:
        answer1 = c + q
    answer2: int = r

    stdout.write("%d %d %d %d %d %d\n" % (a, b, c, d, q, r))
    stdout.write("%d %d\n" % (answer1, answer2))


if __name__ == "__main__":
    solution()