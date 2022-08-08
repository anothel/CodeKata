from sys import stdin, stdout
import sys


def openDoor(open: int) -> int:
    return 1 if open == 0 else 0


def solution():
    n: int = int(stdin.readline().rstrip())
    open: int = int(stdin.readline().rstrip())
    answer: list = list()
    before: int = 0
    bae2: int = openDoor(open)
    bae3: int = open
    for i in range(n - 1):
        before = open
        open = openDoor(open)
        if i % 2 == 0:
            if bae2 != open:
                stdout.write("Love is open door")
                return
        if i % 3 == 1:
            if bae3 != open:
                stdout.write("Love is open door")
                return
        if before == open:
            stdout.write("Love is open door")
            return
        answer.append(open)
    for i in answer:
        stdout.write("%d\n" % i)


if __name__ == "__main__":
    solution()
