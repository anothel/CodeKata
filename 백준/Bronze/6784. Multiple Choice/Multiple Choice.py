from sys import stdin


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    c = []
    for _ in range(N):
        c += (stdin.readline().strip())
    a = []
    for _ in range(N):
        a += (stdin.readline().strip())

    result = 0
    for i in range(N):
        if c[i] == a[i]:
            result += 1
    print(result)
