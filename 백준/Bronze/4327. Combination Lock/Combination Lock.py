from sys import stdin, stdout


def solution():
    while True:
        nums: list = list(map(int, stdin.readline().rstrip().split()))

        if sum(nums) == 0:
            break

        answer: int = 0
        s: int = nums[0]
        n: int = 40
        t1: int = nums[1]
        t2: int = nums[2]
        t3: int = nums[3]

        # 2 full revolutions for the first spin
        answer += 2 * n

        # Go from s to t1, moving backwards in numbers
        if s > t1:
            answer += s - t1
        else:
            answer += s + n - t1

        # 1 full revolution
        answer += n

        # Go from t1 to t2, moving forwards in numbers
        if t1 < t2:
            answer += t2 - t1
        else:
            answer += t2 + n - t1

        # Go from t2 to t3, moving backwards in numbers
        if t2 > t3:
            answer += t2 - t3
        else:
            answer += t2 + n - t3

        stdout.write("%d\n" % (answer * 9))


if __name__ == "__main__":
    solution()
