from sys import stdin, stdout


def solution():
    while True:
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        if sum(nums) == 0:
            break
        answer: int = 0
        n: int = nums[0]
        t1: int = nums[1]
        t2: int = nums[2]
        t3: int = nums[3]

        # answer += (3 * n - 1)
        # answer += (2 * n + t1 - t2)
        # answer += (t3 - t2)
        
        #2 full revolutions for the first spin
        answer += 2 * n        
        #n-1 more ticks to get to t1, if we start at t1 - 1
        answer += (n - 1)
        
        #1 full revolution        
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

        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
