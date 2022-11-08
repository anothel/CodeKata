from sys import stdin, stdout


def solution():
    number: list = list(stdin.readline().rstrip())
    b: int = 0
    r: int = 0
    for i in range(len(number) // 2):
        b += int(number[i])
    for i in range(len(number) // 2, len(number)):
        r += int(number[i])

    stdout.write("LUCKY\n" if b == r else "READY\n")


if __name__ == "__main__":
    solution()