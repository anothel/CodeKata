from sys import stdin




def solution(x):
    if x >=13:
        x += 1
    print(x)


if __name__ == "__main__":
    x = int(stdin.readline().strip())

    solution(x)
