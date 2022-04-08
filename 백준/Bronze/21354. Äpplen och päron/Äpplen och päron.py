from sys import stdin, stdout


def main():
  a, b = map(int, stdin.readline().rstrip().split())

  a *= 7
  b *= 13

  if a < b:
    stdout.write(str("Petra"))
  elif b < a:
    stdout.write(str("Axel"))
  else:
    stdout.write(str("lika"))


if __name__ == "__main__":
  main()
