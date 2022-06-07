from sys import stdin, stdout


def insertValue(nums: list, n: list):
  for _ in range(n):
    nums.append(list(map(int, stdin.readline().rstrip().split())))


def solve():
  n, m = map(int, stdin.readline().rstrip().split())
  a: list = list()
  b: list = list()

  insertValue(a, n)
  insertValue(b, n)

  for i in range(n):
    for j in range(m):
      stdout.write("%d " % (a[i][j] + b[i][j]))
    stdout.write("\n")


if __name__ == "__main__":
    solve()
