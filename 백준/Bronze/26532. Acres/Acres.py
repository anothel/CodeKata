from sys import stdin, stdout
import math

def solution():
    a, b = map(int, stdin.readline().rstrip().split())
    
    stdout.write("%d\n" % (math.ceil(a * b / 4840 / 5)))


if __name__ == "__main__":
    solution()
