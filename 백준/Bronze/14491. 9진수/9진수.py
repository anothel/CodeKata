from sys import stdin, stdout


def solution(n: int, q: int) -> str:
    rev_base: str = str()

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def solve():
  stdout.write("%s\n" % solution(int(stdin.readline().strip()), 9))


if __name__ == "__main__":
    solve()
