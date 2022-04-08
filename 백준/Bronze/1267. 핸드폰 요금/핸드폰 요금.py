from sys import stdin, stdout


def main():
  n = int(stdin.readline().rstrip())
  calls: list = list(map(int, stdin.readline().rstrip().split()))

  young: int = 0
  mins: int = 0

  for i in calls:
    young += ((i // 30) + 1) * 10
    mins += ((i // 60) + 1) * 15

  if young > mins:
    stdout.write(str("M ") + str(mins))
  elif young < mins:
    stdout.write(str("Y ") + str(young))
  else:
    stdout.write(str("Y M ") + str(young))


if __name__ == "__main__":
  main()
