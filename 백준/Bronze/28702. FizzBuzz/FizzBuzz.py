from sys import stdin


def FizzBuzz(nNum):
    if nNum % 3 == 0 and nNum % 5 == 0:
        return "FizzBuzz"
    elif nNum % 3 == 0:
        return "Fizz"
    elif nNum % 5 == 0:
        return "Buzz"
    else:
        return str(nNum)


def solution():
    nMyNumber = 0

    bIsDigitA = False
    bIsDigitB = False
    bIsDigitC = False

    A = str(stdin.readline().strip())
    if A.isdigit():
        bIsDigitA = True
    B = str(stdin.readline().strip())
    if B.isdigit():
        bIsDigitB = True
    C = str(stdin.readline().strip())
    if C.isdigit():
        bIsDigitC = True

    if bIsDigitA == True:
        nMyNumber = int(A) + 3
    if bIsDigitB == True:
        nMyNumber = int(B) + 2
    if bIsDigitC == True:
        nMyNumber = int(C) + 1

    print(FizzBuzz(nMyNumber))


if __name__ == "__main__":
    solution()
