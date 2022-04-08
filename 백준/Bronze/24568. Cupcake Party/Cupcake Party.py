from sys import stdin, stdout


r: int = int(stdin.readline().strip())
s: int = int(stdin.readline().strip())
stdout.write(str(((r*8) + (s*3)) - 28 ))
