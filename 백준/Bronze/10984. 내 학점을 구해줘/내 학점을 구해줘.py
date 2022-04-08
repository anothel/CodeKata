from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().rstrip())):
    nTotalCount:int = 0
    nTotalScore:int = 0
    for _ in range(int(stdin.readline().rstrip())):
      c, g = map(float, stdin.readline().rstrip().split())
      nTotalCount += c
      nTotalScore += c * g
    stdout.write(str(int(nTotalCount)) + " " + str( round(nTotalScore/nTotalCount, 1)) + "\n")

if __name__ == "__main__":
  main()
