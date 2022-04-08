from sys import stdin, stdout


def main():
  n, h, v = map(int, stdin.readline().strip().split())
  
  stdout.write(
      str( 4 * max((n - h) * (n - v),  (n - h) * (v),  (h) * (n - v),  (h) * (v))))


if __name__ == "__main__":
    main()
