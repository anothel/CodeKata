from sys import stdin, stdout


def main():
  n = int(stdin.readline().strip())

  for i in range(1, n+1):
    for _ in range(i):
      stdout.write(str("*"))
    stdout.write(str("\n"))

  n -= 1
  for i in range(n):
    for _ in range(n-i):
      stdout.write(str("*"))
    stdout.write(str("\n"))


if __name__ == "__main__":
    main()
