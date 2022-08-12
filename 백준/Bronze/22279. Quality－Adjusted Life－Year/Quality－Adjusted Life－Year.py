from posixpath import split
from sys import stdin, stdout

if __name__ == "__main__":
    answer: float = 0
    for _ in range(int(stdin.readline().rstrip())):
        q, y = map(float, stdin.readline().rstrip().split())
        answer += q * y
    stdout.write("%f\n" % answer)