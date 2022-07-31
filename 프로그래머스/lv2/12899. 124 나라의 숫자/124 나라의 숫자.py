from sys import stdin, stdout
import math


def solution(n):
    nums: list = ["1", "2", "4"]
    answer = ""
    while n > 0:
        n -= 1
        answer = nums[n % 3] + answer
        n //= 3
    return answer


if __name__ == "__main__":
    n = 8
    print(solution(n))