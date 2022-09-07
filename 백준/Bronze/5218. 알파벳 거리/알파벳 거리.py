from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        x, y = map(str, stdin.readline().rstrip().split())
        stdout.write("Distances:")
        for i in range(len(x)):
            answer: int = 0
            a: int = ord(x[i])
            b: int = ord(y[i])
            if b >= a:
                answer = b - a
            else:
                answer = b + 26 - a
            stdout.write(" %d" % answer)
        stdout.write("\n")


if __name__ == "__main__":
    solution()
