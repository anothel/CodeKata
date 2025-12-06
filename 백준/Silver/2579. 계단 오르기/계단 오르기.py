from sys import stdin


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    steps = [0]
    for _ in range(N):
        h = int(stdin.readline().strip())
        steps.append(h)

    if N == 1:
        print(steps[1])
    elif N == 2:
        print(steps[1] + steps[2])
    else:
        dp = [0] * (N + 1)
        dp[1] = steps[1]
        dp[2] = steps[1] + steps[2]
        dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])

        for i in range(4, N + 1):
            dp[i] = max(dp[i - 2] + steps[i],
                        dp[i - 3] + steps[i - 1] + steps[i])

        print(dp[N])
