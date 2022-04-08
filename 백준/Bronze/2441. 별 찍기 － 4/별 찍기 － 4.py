from sys import stdin, stdout


def main():
  n = int(stdin.readline().rstrip())

  for i in range(n):
    for _ in range(i):
      stdout.write(str(" "))
    for _ in range(n - i):
      stdout.write(str("*"))
    stdout.write(str("\n"))


if __name__ == "__main__":
  main()
