from sys import stdin, stdout


def solution():
    while True:
        n: int = int(stdin.readline().rstrip())
        if n == 0:
            break
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                stdout.write("*")
            stdout.write("\n")


if __name__ == "__main__":
    solution()