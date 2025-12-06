from sys import stdin

if __name__ == "__main__":
    N, M = map(int, stdin.readline().strip().split())
    values = [0]
    values += list(map(int, stdin.readline().strip().split()))

    prefix = [0] * (N + 1)

    for i in range(1, N+1):
        prefix[i] = prefix[i-1]+values[i]

    for _ in range(M):
        i, j = map(int, stdin.readline().strip().split())

        print(prefix[j] - prefix[i-1])
