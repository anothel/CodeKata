from sys import stdin, stdout


def main():
  n = int(stdin.readline().strip())

  for i in range(1, n+1):
    for _ in range(n-i):
      stdout.write(str(" "))
    for _ in range(i):
      stdout.write(str("*"))
    stdout.write(str("\n"))

  for i in range(1, n):
    for _ in range(i):
      stdout.write(str(" "))
    for _ in range(n-i):
      stdout.write(str("*"))
    stdout.write(str("\n"))


if __name__ == "__main__":
    main()
