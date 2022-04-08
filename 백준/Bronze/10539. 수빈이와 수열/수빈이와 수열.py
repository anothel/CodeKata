from sys import stdin, stdout


def main():
  _ = int(stdin.readline().rstrip())
  nums: list = list(map(int, stdin.readline().rstrip().split()))
  answers: list = list()
  for i in range(1, len(nums) + 1):
    tmp: int = 0
    for j in answers:
      tmp += j
    answers.append(nums[i-1] * i - tmp)

  for i in answers:
    stdout.write(str(i) + " ")


if __name__ == "__main__":
  main()
