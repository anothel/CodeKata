from sys import stdin, stdout


def cal(money: int) -> str:
  q: int = int(money / 25)
  money %= 25
  d: int = int(money / 10)
  money %= 10
  n: int = int(money / 5)
  money %= 5
  p: int = int(money / 1)
  money %= 1

  return str(str(q) + " " + str(d) + " " + str(n) + " " + str(p))


def main():
  for _ in range(int(stdin.readline().rstrip())):
    stdout.write(cal(int(stdin.readline().rstrip())) + "\n")


if __name__ == "__main__":
  main()
