from sys import stdin, stdout


def main():
  a = int(stdin.readline().strip())
  x = int(stdin.readline().strip())
  b = int(stdin.readline().strip())
  y = int(stdin.readline().strip())
  T = int(stdin.readline().strip())

  if T > 30:
    a += (T - 30) * x * 21
  if T > 45:
    b += (T - 45) * y * 21

  stdout.write(str(a) + " " + str(b))


if __name__ == "__main__":
    main()
