from sys import stdin, stdout


def main():
  nTotal: int = 0
  nMax: int = 0
  for _ in range(10):
    nOut, nIn = map(int, stdin.readline().rstrip().split())
    nTotal += (-nOut + nIn)
    if nTotal > nMax:
      nMax = nTotal

  stdout.write(str(nMax))


if __name__ == "__main__":
    main()
