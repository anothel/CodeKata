from sys import stdin


if __name__ == "__main__":
    N = int(stdin.readline().strip())

    D = 0
    P = 0
    for i in range(1, N+1):
        r = (stdin.readline().strip())
        if r == 'D':
            D += 1
        else:
            P += 1
        if abs(D-P) == 2:
            break
    print(f"{D}:{P}")
