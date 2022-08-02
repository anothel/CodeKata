from sys import stdin, stdout


def solution():
    vowels: list = ["a", "e", "i", "o", "u"]

    s: str = stdin.readline().rstrip()
    count: int = 0
    for i in s:
        if i in vowels:
            count += 1
    stdout.write("%d\n" % count)


if __name__ == "__main__":
    solution()
