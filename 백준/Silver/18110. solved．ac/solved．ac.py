from sys import stdin


def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def solution():
    n = int(stdin.readline().strip())
    arr = []
    u15 = int(round2(n*0.15))

    for _ in range(n):
        value = int(stdin.readline().strip())
        arr.append(value)
    arr = quick_sort(arr)
    arr = arr[u15:n-u15]
    if len(arr) == 0:
        print(0)
    else:
        print(round2(sum(arr)/len(arr)))


if __name__ == "__main__":
    solution()
