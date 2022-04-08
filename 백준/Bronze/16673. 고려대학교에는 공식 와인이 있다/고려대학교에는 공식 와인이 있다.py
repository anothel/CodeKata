from sys import stdin, stdout


def solved():
  nums: list = list(map(int, stdin.readline().rstrip().split()))

  nAns: int = 0
  k: int = nums[1]
  p: int = nums[2]
  for n in range(1, nums[0] + 1):
    nAns += k*n+p*(n**2)

  stdout.write(str(nAns))


def main():
  solved()


if __name__ == "__main__":
    main()
