from sys import stdin, stdout


def solve():
    n, m = map(int, stdin.readline().rstrip().split())
    friends: dict = {i: 0 for i in range(1, n + 1)}
    for _ in range(m):
        a, b = map(int, stdin.readline().rstrip().split())
        friends[a] += 1
        friends[b] += 1
    for i in range(1, n + 1):
        stdout.write("%d\n" % friends[i])


if __name__ == "__main__":
    solve()
