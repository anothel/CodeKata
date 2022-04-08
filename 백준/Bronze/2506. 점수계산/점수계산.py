from sys import stdin, stdout


def main():
  nBefore: int = 0
  int(stdin.readline().rstrip())
  nRv: int = 0
  
  for i in list(map(int, stdin.readline().rstrip().split())):
    if i == 1:
      nBefore += 1
      nRv += nBefore
    else:
      nBefore = 0

  stdout.write(str(nRv))


if __name__ == "__main__":
    main()
