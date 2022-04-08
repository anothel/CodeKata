from sys import stdin, stdout


def main():
  n, w, h = map(int, stdin.readline().rstrip().split())
  for _ in range(n):
    s: int = int(stdin.readline().rstrip())
    if s <= w or s <= h or s <= (w**2+h**2)**0.5:
      stdout.write("DA\n")
    else:
      stdout.write(str("NE\n"))


if __name__ == "__main__":
  main()
