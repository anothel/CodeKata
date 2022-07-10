from sys import stdin, stdout


def solution():
    _nums1: list = [1, 2, 3, 3, 4, 10]
    _nums2: list = [1, 2, 2, 2, 3, 5, 10]
    for i in range(int(stdin.readline().rstrip())):
        stdout.write("Battle %d: " % (i + 1))
        num1: list = list(map(int, stdin.readline().rstrip().split()))
        for j in range(len(num1)):
            num1[j] *= _nums1[j]

        num2: list = list(map(int, stdin.readline().rstrip().split()))
        for k in range(len(num2)):
            num2[k] *= _nums2[k]

        if sum(num1) > sum(num2):
            stdout.write("Good triumphs over Evil\n")
        elif sum(num2) > sum(num1):
            stdout.write("Evil eradicates all trace of Good\n")
        else:
            stdout.write("No victor on this battle field\n")


if __name__ == "__main__":
    solution()
