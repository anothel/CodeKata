from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())

    stdout.write(
        "yes\n" if sum(list(map(int,
                                stdin.readline().rstrip().split()))) %
        3 == 0 else "no\n")


if __name__ == "__main__":
    solution()
