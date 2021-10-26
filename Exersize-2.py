n = abs(int(input("Please enter n : ")))
m = abs(int(input("Please enter m : ")))
while (n == 0 or m == 0):
    n = abs(int(input("Please enter n (It can\'t be zero or negative) : ")))
    m = abs(int(input("Please enter m (It can\'t be zero or negative) : ")))
i = 0
j = 0
cnt = 0
n += 1
m += 1
for i in range(n):
    for j in range(m):
        if (cnt == 0):
            print('#',end = '')
            cnt = 1
        else:
            print('*',end = '')
            cnt = 0
    print()