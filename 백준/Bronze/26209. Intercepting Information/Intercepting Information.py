from sys import stdin, stdout


def solution():
    nums: list = list(map(int, stdin.readline().rstrip().split(' ')))

    for i in nums:
        if i != 1 and i != 0:
            stdout.write("F")
            return
    stdout.write("S")


if __name__ == "__main__":
    solution()
