from sys import stdin, stdout


def main():
  b = int(stdin.readline().rstrip())
  p: int = 5 * b - 400
  stdout.write(str(p) + "\n")

  if p < 100:
    stdout.write(str(1))
  elif 100 < p:
    stdout.write(str(-1))
  else:
    stdout.write(str(0))


if __name__ == "__main__":
  main()
