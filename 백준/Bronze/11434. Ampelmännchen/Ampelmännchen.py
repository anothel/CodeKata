from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        n, W, E = map(int, stdin.readline().rstrip().split())
        answer: int = 0

        for _ in range(n):
            Lww, Lwe, Lew, Lee = map(int, stdin.readline().rstrip().split())
            answer += max(Lww * W + Lew * E, Lwe * W + Lee * E)

        stdout.write("Data Set %d:\n" % (i + 1))
        stdout.write("%d\n" % answer)
        stdout.write("\n")


if __name__ == "__main__":
    solution()
