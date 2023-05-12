from sys import stdin


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        if nums[0] * nums[1] > nums[2] * nums[3]:
            print('TelecomParisTech')
        elif nums[0] * nums[1] < nums[2] * nums[3]:
            print('Eurecom')
        else:
            print('Tie')


if __name__ == "__main__":
    solution()
