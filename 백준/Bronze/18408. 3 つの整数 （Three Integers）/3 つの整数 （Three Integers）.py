from sys import stdin, stdout


def main():
  nums = list(map(int, stdin.readline().rstrip().split()))
  stdout.write(str("1" if nums.count(2) < nums.count(1) else "2"))


if __name__ == "__main__":
  main()
