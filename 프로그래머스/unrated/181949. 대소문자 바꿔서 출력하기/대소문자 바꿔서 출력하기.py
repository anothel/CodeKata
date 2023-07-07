str = input()
a = ''
for i in range(len(str)):
    if str[i].isupper():
        a = a + str[i].lower()
    else :
        a = a + str[i].upper()
print(a)