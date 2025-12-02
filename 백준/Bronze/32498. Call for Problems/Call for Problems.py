from sys import stdin





if __name__ == "__main__":
    n = int(stdin.readline().strip())
    ans = 0
    for _ in range(n):
        d = int(stdin.readline().strip())
        if d % 2 != 0:
            ans += 1
    print(ans)

