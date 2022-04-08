from sys import stdin, stdout


def main():
  num = int(stdin.readline().rstrip())
  nums = list(map(int, stdin.readline().rstrip().split()))

  stdout.write(str(nums.count(num)))


if __name__ == "__main__":
    main()
