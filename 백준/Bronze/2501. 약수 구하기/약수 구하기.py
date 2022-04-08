from sys import stdin, stdout


def main():
  nums: list = list()

  n, k = map(int, stdin.readline().rstrip().split())

  for i in range(1, n+1):
    if n % i == 0:
      nums.append(i)

  # stdout.write(str(sorted(set(nums))))
  if len(nums) < k:
    stdout.write(str(0))
  else:
    stdout.write(str(sorted(set(nums))[k-1]))


if __name__ == "__main__":
    main()
