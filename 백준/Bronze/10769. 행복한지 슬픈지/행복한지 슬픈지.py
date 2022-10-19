from sys import stdin, stdout


def solution():
    sen: str = stdin.readline().rstrip()

    answer: str = 'none'

    if sen.count(':-)') > sen.count(':-('):
        answer = 'happy'
    elif sen.count(':-)') < sen.count(':-('):
        answer = 'sad'
    elif sen.count(':-)') == 0 and sen.count(':-(') == 0:
        answer = 'none'
    elif sen.count(':-)') == sen.count(':-('):
        answer = 'unsure'

    stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solution()