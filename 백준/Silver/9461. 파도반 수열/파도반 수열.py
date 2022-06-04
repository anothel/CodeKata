from sys import stdin, stdout


def solve():
  dp: list = [0] * 101
  dp[0] = 0
  dp[1] = 1
  dp[2] = 1
  dp[3] = 1
  for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

  for _ in range(int(stdin.readline().rstrip())):
    stdout.write("%d\n" % dp[int(stdin.readline().rstrip())])


if __name__ == "__main__":
    solve()
