from sys import stdin, stdout


def track(a: float, b: float, c: float, p: int) -> int:
    return int(a * ((b - p)**c))


def field(a: float, b: float, c: float, p: int) -> int:
    return int(a * ((p - b)**c))


def solve():
    for _ in range(int(stdin.readline().rstrip())):
        answer: int = 0
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        for i in range(len(nums)):
            if i == 0:
                answer += track(9.23076, 26.7, 1.835, nums[i])
            elif i == 1:
                answer += field(1.84523, 75, 1.348, nums[i])
            elif i == 2:
                answer += field(56.0211, 1.5, 1.05, nums[i])
            elif i == 3:
                answer += track(4.99087, 42.5, 1.81, nums[i])
            elif i == 4:
                answer += field(0.188807, 210, 1.41, nums[i])
            elif i == 5:
                answer += field(15.9803, 3.8, 1.04, nums[i])
            elif i == 6:
                answer += track(0.11193, 254, 1.88, nums[i])

        stdout.write("%d\n" % int(answer))


if __name__ == "__main__":
    solve()
