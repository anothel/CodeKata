from sys import stdin


def solution(arr):
    arr.sort()
    for i in range(len(arr)):
        if i + 1 == arr[i]:
            continue
        else:
            print(i + 1)
            return
    print(len(arr) + 1)
    return


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))

    solution(arr)
