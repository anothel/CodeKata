from sys import stdin, stdout


def main():
  # n = int(stdin.readline().strip())
  N, M = map(int, stdin.readline().strip().split())

  if M == 1 or M == 2:
    stdout.write(str("NEWBIE!"))
  elif M <= N:
    stdout.write(str("OLDBIE!"))
  else:
    stdout.write(str("TLE!"))


if __name__ == "__main__":
  main()
