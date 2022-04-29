from sys import stdin, stdout


def solve():
  s1, s2 = map(int, stdin.readline().rstrip().split())
  bSample: bool = True
  bSystem: bool = True
  for _ in range(s1):
    mine, answer = map(int, stdin.readline().rstrip().split())
    if mine != answer:
      bSample = False
      break
  for _ in range(s2):
    mine, answer = map(int, stdin.readline().rstrip().split())
    if mine != answer:
      bSystem = False
      break
  if bSample == True and bSystem == True:
    stdout.write("Accepted\n")
  elif bSample == False:
    stdout.write("Wrong Answer\n")
  elif bSample == True and bSystem == False:
    stdout.write("Why Wrong!!!\n")


if __name__ == "__main__":
    solve()
