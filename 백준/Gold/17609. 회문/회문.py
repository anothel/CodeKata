from sys import stdin


def IsAlmostPal(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return IsPal(s[left+1:right+1]) or IsPal(s[left:right])
        left += 1
        right -= 1
    return False


def IsPal(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def solution(arr):
    for s in arr:
        if IsPal(s) == True:
            print("0")
        elif IsAlmostPal(s) == True:
            print("1")
        else:
            print("2")


if __name__ == "__main__":
    T = int(stdin.readline().strip())
    arr = []
    for _ in range(T):
        arr.append(str(stdin.readline().strip()))
    solution(arr)
