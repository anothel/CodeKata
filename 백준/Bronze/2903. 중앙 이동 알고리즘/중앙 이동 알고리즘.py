from sys import stdin, stdout


def main():
  n = int(stdin.readline().rstrip())

  point: int = 2
  for _ in range(n):
    point += (point - 1)

  stdout.write(str(point**2))


if __name__ == "__main__":
  main()
