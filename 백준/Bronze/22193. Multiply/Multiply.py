from sys import stdin, stdout


N, M = map(int, stdin.readline().strip().split())
A: int = int(stdin.readline().strip())
B: int = int(stdin.readline().strip())

stdout.write(str(A * B))
