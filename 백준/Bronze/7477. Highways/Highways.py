from sys import stdin


def solution(arr):
    n = len(arr) + 1
    xs = [0] + arr

    if n < 4:
        print(0)
        return

    gaps = [xs[i+1] - xs[i] for i in range(n-1)]

    best_idx = -1
    best_gap = 10**30
    for i in range(1, n-2):
        if gaps[i] < best_gap:
            best_gap = gaps[i]
            best_idx = i

    total = xs[-1] + best_gap

    gap_left_city = best_idx + 1
    gap_right_city = best_idx + 2

    S1, E1 = gap_right_city, 1
    S2, E2 = n, gap_left_city

    print(total)
    print(S1, E1, S2, E2)


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))

    if N < 4:
        print("0")
    else:
        solution(arr)
