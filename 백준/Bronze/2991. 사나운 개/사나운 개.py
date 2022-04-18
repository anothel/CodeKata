from sys import stdin, stdout


def wildDog(attack: int, breath: int, myTime: int) -> int:
  tmp: int = myTime % (attack + breath)
  if tmp == 0:
    tmp = attack + breath
  return 1 if tmp <= attack else 0


def solve():
  a, b, c, d = map(int, stdin.readline().strip().split())
  for i in list(map(int, stdin.readline().strip().split())):
    stdout.write("%d\n" % (wildDog(a, b, i) + wildDog(c, d, i)))


if __name__ == "__main__":
    solve()
