from sys import stdin, stdout


def solution():
    worth: int = 0
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    for i in range(3):
        mul: int = 0
        if i == 0:
            mul = 3
        elif i == 1:
            mul = 2
        elif i == 2:
            mul = 1
        worth += nums[i] * mul

    if worth >= 8:
        stdout.write("Province or Gold")
    elif worth >= 6:
        stdout.write("Duchy or Gold")
    elif worth >= 5:
        stdout.write("Duchy or Silver")
    elif worth >= 3:
        stdout.write("Estate or Silver")
    elif worth >= 2:
        stdout.write("Estate or Copper")
    elif worth >= 0:
        stdout.write("Copper")


if __name__ == "__main__":
    solution()
