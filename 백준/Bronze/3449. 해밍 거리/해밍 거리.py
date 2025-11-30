from sys import stdin


def solution(x1, x2):
    n = len(x1)
    count = 0
    for i in range(n):
        if x1[i] != x2[i]:
            count += 1
    print(f"Hamming distance is {count}.")
    

if __name__ == "__main__":
    T = int(stdin.readline().strip())
    for _ in range(T):
        x1 = stdin.readline().strip()
        x2 = stdin.readline().strip()
        solution(x1,x2)
