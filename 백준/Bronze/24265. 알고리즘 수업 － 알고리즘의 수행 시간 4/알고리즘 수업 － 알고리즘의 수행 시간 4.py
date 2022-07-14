from sys import stdin, stdout


def MenOfPassion(A: list, n: int) -> int:
    sum: int = 0
    count: int = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            sum += A[i] * A[j]  # 코드1
            count += 1
    return count


def solve():
    a: list = [1] * 500000
    n: int = int(stdin.readline().rstrip())
    stdout.write("%d\n" % (n * (n-1) // 2))
    stdout.write("2\n")


if __name__ == "__main__":
    solve()
