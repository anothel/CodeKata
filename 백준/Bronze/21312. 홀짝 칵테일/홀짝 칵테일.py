from sys import stdin, stdout


def solve():
    a, b, c = map(int, stdin.readline().rstrip().split())

    oddMax: int = 0
    evenMax: int = 0
    if a % 2 != 0 and oddMax < a:
        oddMax = a
    if b % 2 != 0 and oddMax < b:
        oddMax = b
    if c % 2 != 0 and oddMax < c:
        oddMax = c
    if a * b % 2 != 0 and oddMax < a * b:
        oddMax = a * b
    if a * c % 2 != 0 and oddMax < a * c:
        oddMax = a * c
    if b * c % 2 != 0 and oddMax < b * c:
        oddMax = b * c
    if a * b * c % 2 != 0 and oddMax < a * b * c:
        oddMax = a * b * c

    if oddMax == 0:
        if evenMax < a:
            evenMax = a
        if evenMax < b:
            evenMax = b
        if evenMax < c:
            evenMax = c
        if evenMax < a * b:
            evenMax = a * b
        if evenMax < a * c:
            evenMax = a * c
        if evenMax < b * c:
            evenMax = b * c
        if evenMax < a * b * c:
            evenMax = a * b * c
        stdout.write("%d\n" % evenMax)
    else:
        stdout.write("%d\n" % oddMax)


if __name__ == "__main__":
    solve()
