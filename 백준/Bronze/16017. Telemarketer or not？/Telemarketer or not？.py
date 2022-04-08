from sys import stdin, stdout


def main():
  m1 = int(stdin.readline().strip())
  m2 = int(stdin.readline().strip())
  m3 = int(stdin.readline().strip())
  m4 = int(stdin.readline().strip())

  if (m1 == 8 or m1 == 9) and (m4 == 8 or m4 == 9) and (m2 == m3):
    stdout.write(str("ignore"))
  else:
    stdout.write(str("answer"))


if __name__ == "__main__":
    main()
