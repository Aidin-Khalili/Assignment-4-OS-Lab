n = abs(int(input("Please enter n : ")))
i = 0
arr_fibo = [0,1]
if n != 0:
    for i in range(2,n):
        arr_fibo.append(arr_fibo[i-1] + arr_fibo[i-2])
    print(arr_fibo)
elif n == 0:
    print(arr_fibo[0])