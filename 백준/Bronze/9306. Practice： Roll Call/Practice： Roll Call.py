from sys import stdin


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    c = []
    for _ in range(N):
        f = (stdin.readline().strip())
        l = (stdin.readline().strip())
        c.append((l, f))

    for i in range(N):
        print(f"Case {i+1}: {c[i][0]}, {c[i][1]}")
