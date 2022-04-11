from sys import stdin, stdout


def getNext(input: int) -> int:
  return input//2 if input % 2 == 0 else (3 * input + 1)


def solve():
  n: int = 1
  before: int = int(stdin.readline().rstrip())
  while before != 1:
    before = getNext(before)
    n += 1

  stdout.write(str(n))


def main():
  solve()


if __name__ == "__main__":
    main()
