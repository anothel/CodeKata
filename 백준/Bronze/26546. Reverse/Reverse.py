from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        s, i, j = (map(str, stdin.readline().rstrip().split()))
        i = int(i)
        j = int(j)
        for k in range(len(s)):
            if i <= k and k < j:
                continue
            stdout.write("%s" % (s[k]))
        stdout.write("\n")


if __name__ == "__main__":
    solution()
