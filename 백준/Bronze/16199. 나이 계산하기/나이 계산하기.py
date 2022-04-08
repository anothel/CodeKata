from sys import stdin, stdout


def main():
  y, m, d = map(int, stdin.readline().rstrip().split())
  y1, m1, d1 = map(int, stdin.readline().rstrip().split())

  man: int = 0
  sae: int = 0
  yea: int = 0
  if y1 > y:
    sae = y1 - y + 1
    yea = y1 - y
    if m1 > m:
      man = y1 - y
    elif m1 == m:
      if d1 >= d:
        man = y1 - y
      else:
        man = y1 - y - 1
    else:
        man = y1 - y - 1
  elif y1 == y:
    man = 0
    sae = 1
    yea = 0

  stdout.write(str(man) + "\n")
  stdout.write(str(sae) + "\n")
  stdout.write(str(yea))


if __name__ == "__main__":
    main()
