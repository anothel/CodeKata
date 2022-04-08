from sys import stdin, stdout


def main():
  n = int(stdin.readline().strip())

  for _ in range(n - 1):
    stdout.write(str(" "))

  stdout.write(str("*\n"))

  for i in range(1, n):
    for _ in range(n - i - 1):
      stdout.write(str(" "))
    for j in range(i):
      stdout.write(str("*" if (j == 0)  else " "))

    stdout.write(str(" " ))

    for j in range(i):
      stdout.write(str("*" if (j == i-1)  else " "))
    stdout.write(str("\n"))


if __name__ == "__main__":
    main()
#    *
#   * *
#  *   *
# *     *