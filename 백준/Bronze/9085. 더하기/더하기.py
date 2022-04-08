from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().strip())):
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().rstrip().split()))
    stdout.write(str(sum(nums)) + "\n")


if __name__ == "__main__":
    main()
