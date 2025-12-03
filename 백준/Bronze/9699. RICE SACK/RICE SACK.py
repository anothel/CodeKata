from sys import stdin


if __name__ == "__main__":
    N = int(stdin.readline().strip())

    for i in range(1, N+1):
        m = map(int, (stdin.readline().strip().split()))
        print(f"Case #{i}: {max(m)}")
