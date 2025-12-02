from sys import stdin




def solution(a,b,c):

    if a+b+c<=21:
        print("1")
    else:
        print("0")


if __name__ == "__main__":
    a = int(stdin.readline().strip())
    b = int(stdin.readline().strip())
    c = int(stdin.readline().strip())
    

    solution(a,b,c)
