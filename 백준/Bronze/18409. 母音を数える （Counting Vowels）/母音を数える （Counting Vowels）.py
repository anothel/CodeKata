from sys import stdin, stdout


def solution():
  words: list = ["a", "e", "i", "o", "u"]
  n: int = int(stdin.readline().rstrip())
  s: str = stdin.readline().rstrip().lower()
  count: int = 0
  for i in s:
    if i in words:
      count += 1
  stdout.write("%d\n" % count)


if __name__ == "__main__":
  solution()
