from sys import stdin, stdout


A,B,C,D = map(int, stdin.readline().strip().split())

stdout.write(str(A * 56 + B*24+14*C+6*D ))
