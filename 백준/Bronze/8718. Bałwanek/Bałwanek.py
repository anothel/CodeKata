from sys import stdin, stdout


def main():
  x, k = map(int, stdin.readline().strip().split())

  if 7 * k <= x:
    print(k*7000)
  elif 3.5 * k <= x:
    print(k*3500)
  elif 1.75 * k <= x:
    print(k*1750)
  else:
    print(0)

  # print((w-k)//m + (1 if (w-k) % m else 0))


if __name__ == "__main__":
  main()
