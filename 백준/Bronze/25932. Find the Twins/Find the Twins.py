from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    for _ in range(n):
        z: bool = False
        m: bool = False
        nums: list = list(map(int, stdin.readline().rstrip().split()))

        for i in nums:
            if i == 17:
                z = True
            elif i == 18:
                m = True
            stdout.write("%d " % (i))
        if z == True and m == True:
            stdout.write("\nboth\n")
        elif z == False and m == False:
            stdout.write("\nnone\n")
        elif z == True:
            stdout.write("\nzack\n")
        elif m == True:
            stdout.write("\nmack\n")
        stdout.write("\n")


if __name__ == "__main__":
    solution()
