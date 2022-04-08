from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().rstrip())):
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    numsEven: list = list()
    for i in nums:
      if i % 2 == 0:
        numsEven.append(i)
    stdout.write(str(sum(numsEven)) + " " + str(min(numsEven)) + "\n")


if __name__ == "__main__":
  main()
