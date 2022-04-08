from sys import stdin, stdout

total: int = int(stdin.readline().strip())
each: int = int(stdin.readline().strip())

print((total - each) //2 + each)
print((total - each) //2)
    
