n = abs(int(input("Please enter n : ")))
m = abs(int(input("Please enter m : ")))
while (n == 0 or m == 0):
    n = abs(int(input("Please enter n (It can\'t be zero or negative) : ")))
    m = abs(int(input("Please enter m (It can\'t be zero or negative) : ")))
i = j = 1
n += 1
m += 1
for i in range(n):
    for j in range(m):
        if(i==0):
            if(j!=0): print(j, end = ' ')
            else : print('x',end = ' ')
        else:
            if(j!=0): print(i*j , end = ' ')
            else: print(i, end = ' ')
    print()