from sys import stdin, stdout


def solve():
  n: int = 1
  while True:
    n0: int = int(stdin.readline().rstrip())
    if n0 == 0:
      break
    n1: int = (3 * n0)
    isEven: bool = False
    if n1 % 2 == 0:
      isEven = True
    n2: int = 0
    if n1 % 2 == 0:
      n2 = n1//2
    else:
      n2 = (n1+1)//2
    n3: int = 3 * n2
    n4 = n3 // 9

    stdout.write(str("%d. " % n) + str("even " if isEven else "odd ") +
                 str(n4) + "\n")
    n += 1


def main():
  solve()


if __name__ == "__main__":
    main()
