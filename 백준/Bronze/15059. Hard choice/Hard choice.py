from sys import stdin, stdout


def getDiff(a: int, r: int) -> int:
  return r - a if r > a else 0


def main():
  ca, ba, pa = map(int, stdin.readline().rstrip().split())
  cr, br, pr = map(int, stdin.readline().rstrip().split())

  stdout.write(str(getDiff(ca, cr) + getDiff(ba, br) + getDiff(pa, pr)))


if __name__ == "__main__":
    main()
