from sys import stdin, stdout


def main():
  k, w, m = map(int, stdin.readline().strip().split())

  print((w-k)//m + (1 if (w-k) % m else 0))


if __name__ == "__main__":
  main()
