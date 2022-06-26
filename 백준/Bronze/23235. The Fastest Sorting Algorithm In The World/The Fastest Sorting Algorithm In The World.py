from sys import stdin, stdout


def main():
    i: int = 1
    while True:
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        if nums[0] == 0 and len(nums) == 1:
            break
        stdout.write("Case %d: Sorting... done!\n" % i)
        i += 1


if __name__ == "__main__":
    main()
