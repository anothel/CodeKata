from sys import stdin, stdout


def main():
  if int(stdin.readline().rstrip()) == 0:
    stdout.write(str("divide by zero"))
    return
  else:
    nums = list(map(int, stdin.readline().rstrip().split()))

  gidae: float = 0
  for i in set(nums):
    su = nums.count(i)
    l = len(nums)
    gidae += (i * (su / l))

  stdout.write(str("%.2f" % (round((sum(nums) / len(nums))/gidae, 2))))


if __name__ == "__main__":
    main()
