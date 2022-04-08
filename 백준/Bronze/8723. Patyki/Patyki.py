from sys import stdin, stdout


def main():
  a = sorted(map(int, stdin.readline().strip().split()))

  if a[0] == a[1] == a[2]:
    stdout.write("2")
  elif a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
    print(1)
  else:
    print(0)

  # print((w-k)//m + (1 if (w-k) % m else 0))


if __name__ == "__main__":
  main()
