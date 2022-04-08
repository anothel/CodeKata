from sys import stdin, stdout


def main():
  a, b = map(int, stdin.readline().rstrip().split())
  
  total: int = (abs(b - a) + 1) * (a + b) // 2

  stdout.write(str(total))


if __name__ == "__main__":
  main()
