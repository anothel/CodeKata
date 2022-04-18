from sys import stdin, stdout


def solution():
  n, k = map(int, stdin.readline().rstrip().split())
  nums = list(map(int, stdin.readline().rstrip().split()))

  counts: int = 0
  for i in nums:
    if i % 2 != 0:
      counts += (i + 1) // 2
    else:
      counts += i // 2
  stdout.write("YES" if counts >= n else "NO")

  stdout.write("")


if __name__ == "__main__":
    solution()
