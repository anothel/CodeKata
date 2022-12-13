from sys import stdin, stdout


def solution():
    k: str = (stdin.readline().rstrip())
    if 'd2' in k or 'D2' in k:
        stdout.write("D2")
    else:
        stdout.write("unrated")


if __name__ == "__main__":
    solution()
