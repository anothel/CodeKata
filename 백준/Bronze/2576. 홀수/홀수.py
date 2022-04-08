from sys import stdin, stdout


def main():
  num: int = 0
  nums: list = list()
  holExist: bool = False
  for _ in range(7):
    n = int(stdin.readline().strip())
    if n % 2 != 0:
      num += n
      nums.append(n)
      holExist = True
  if holExist:
    stdout.write(str(num) + "\n")
    stdout.write(str(min(nums)) + "\n")
  else:
    stdout.write(str(-1))


if __name__ == "__main__":
    main()
