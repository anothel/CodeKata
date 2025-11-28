from sys import stdin


def answer(N, K, arr):
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    if max(dp) >= K:
        return 1
    else:
        return 0


def solution():
    T = int(stdin.readline().strip())
    for i in range(T):
        N, K = map(int, stdin.readline().split())
        arr = list(map(int, stdin.readline().split()))
        if len(arr) != N:
            raise ValueError("arr length is not correct")
        print("Case #%d" % (i + 1))
        print(answer(N, K, arr))


if __name__ == "__main__":
    solution()
