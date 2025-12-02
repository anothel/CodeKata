from sys import stdin



def solution(arr):

    if arr[0] + arr[1] == arr[2]:
        print("correct!")
    else:
        print("wrong!")


if __name__ == "__main__":
    arr = list(map(int,(stdin.readline().strip().split())))

    solution(arr)
