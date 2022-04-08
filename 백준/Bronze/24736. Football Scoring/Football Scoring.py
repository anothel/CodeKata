from sys import stdin, stdout


def main():
    t1,f1,s1,p1,c1 = map(int,stdin.readline().rstrip().split())
    t2,f2,s2,p2,c2 = map(int,stdin.readline().rstrip().split())
    
    stdout.write(str( t1*6+f1*3+s1*2+p1+c1*2    ) + " " + str( t2*6+f2*3+s2*2+p2+c2*2    ))


if __name__ == "__main__":
  main()

