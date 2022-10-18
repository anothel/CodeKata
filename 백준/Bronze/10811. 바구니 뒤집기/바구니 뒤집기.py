from sys import stdin, stdout


def solution():
    n, m = map(int, stdin.readline().rstrip().split())

    bucket: list = [i for i in range(1, n + 1)]

    for i in range(m):
        i, j = map(int, stdin.readline().rstrip().split())

        tmp: list() = bucket[i - 1:j]
        tmp.reverse()
        
        for k in range(len(bucket)):
            if i - 1 <= k and k < j:
                bucket[k] = tmp[0]
                tmp.remove(tmp[0])
    for i in bucket:
        stdout.write("%d " % i)


if __name__ == "__main__":
    solution()