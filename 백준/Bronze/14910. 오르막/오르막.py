from sys import stdin, stdout


def solution():
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    answer: bool = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            answer = False
            break

    stdout.write("Good\n" if answer == True else "Bad\n")


if __name__ == "__main__":
    solution()
