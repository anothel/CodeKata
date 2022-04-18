from sys import stdin, stdout


def solution():
  n: int = int(stdin.readline().rstrip())
  stars: str = str()
  for i in range(1, n+1):
    if i % 2 == 0:
      for _ in range(n):
        stars += " *"
    else:
      for _ in range(n):
        stars += "* "
    stars += "\n"
  stdout.write(stars)


if __name__ == "__main__":
    solution()
