from sys import stdin


def solution(c):
    if c == 'Algorithm':
        print('204')
    if c == 'DataAnalysis':
        print('207')
    if c == 'ArtificialIntelligence':
        print('302')
    if c == 'CyberSecurity':
        print('B101')
    if c == 'Network':
        print('303')
    if c == 'Startup':
        print('501')
    if c == 'TestStrategy':
        print('105')


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    for _ in range(N):
        c = (stdin.readline().strip())
        solution(c)
