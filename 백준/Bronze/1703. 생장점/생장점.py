from sys import stdin, stdout


def solve():
  while 1:
    leaves: list = list(map(int, input().split()))
    leaf: int = 1
    if leaves[0] == 0:
        break

    for i in range(1, len(leaves), 2):
        leaf = leaf * leaves[i] - leaves[i+1]
    stdout.write("%d\n" % leaf)


if __name__ == "__main__":
    solve()
