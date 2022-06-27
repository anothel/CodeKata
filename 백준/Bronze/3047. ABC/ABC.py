from sys import stdin, stdout


def main():
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))
    sec: list = stdin.readline().rstrip()
    for i in sec:
        if i == "A":
            stdout.write("%d " % nums[0])
        elif i == "B":
            stdout.write("%d " % nums[1])
        elif i == "C":
            stdout.write("%d " % nums[2])


if __name__ == "__main__":
    main()
