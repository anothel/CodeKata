from sys import stdin, stdout


def solution():
  a, b, c = map(int, stdin.readline().rstrip().split())

  if a == b and b == c:
    stdout.write("*")
  elif a == b and b != c:
    stdout.write("C")
  elif b == c and b != a:
    stdout.write("A")
  elif a == c and b != c:
    stdout.write("B")


if __name__ == "__main__":
  solution()
