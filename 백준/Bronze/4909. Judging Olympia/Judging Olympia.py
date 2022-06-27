from sys import stdin, stdout


def solve():
    while True:
        nums = list(map(int, stdin.readline().rstrip().split()))
        if sum(nums) == 0:
            break
        nums.remove(max(nums))
        nums.remove(min(nums))
        stdout.write("%g\n" % (sum(nums) / len(nums)))


if __name__ == "__main__":
    solve()
