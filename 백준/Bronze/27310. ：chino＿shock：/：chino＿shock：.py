from sys import stdin, stdout


def solution():
    s: str = str(stdin.readline().rstrip())

    length: int = len(s)
    colon: int = s.count(':')
    under: int = s.count('_')

    stdout.write("%d\n" % (length + colon + under * 5))


if __name__ == "__main__":
    solution()
