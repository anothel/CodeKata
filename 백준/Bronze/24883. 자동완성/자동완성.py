from sys import stdin, stdout


def solve():
  s: str = stdin.readline().rstrip()
  stdout.write("Naver D2" if s == "N" or s == "n" else "Naver Whale")


def main():
  solve()


if __name__ == "__main__":
    main()
