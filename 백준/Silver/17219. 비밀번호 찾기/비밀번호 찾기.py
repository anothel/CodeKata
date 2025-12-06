from sys import stdin


def findPwd(s, arr):
    return arr[s]


if __name__ == "__main__":
    N, M = map(int, stdin.readline().strip().split())
    arr = {}
    for _ in range(N):
        h, p = stdin.readline().strip().split()
        arr[h] = p

    for _ in range(M):
        s = stdin.readline().strip()
        print(findPwd(s, arr))
