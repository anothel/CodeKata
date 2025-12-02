from sys import stdin




def solution(a,b):

    print(a*1000 + b*10000)


if __name__ == "__main__":
    a = int(stdin.readline().strip())
    b = int(stdin.readline().strip())

    solution(a,b)
