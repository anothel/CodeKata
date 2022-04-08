from sys import stdin, stdout


def main():

  while True:
    nums: list = list(stdin.readline().rstrip())
    if nums[0] == "0":
      break

    total: int = 0
    for n in nums:
      if int(n) == 1:
        total += 2
      elif int(n) == 0:
        total += 4
      else:
        total += 3
    total += (len(nums) + 1)

    stdout.write(str(total) + "\n")


if __name__ == "__main__":
  main()
