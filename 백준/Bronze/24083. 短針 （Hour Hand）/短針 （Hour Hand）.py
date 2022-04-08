from sys import stdin, stdout


def main():
  A = int(stdin.readline().rstrip())
  B = int(stdin.readline().rstrip())

  stdout.write(str((A+B) % 12 if (A+B) % 12 != 0 else 12))


if __name__ == "__main__":
  main()
