n = int(input("please enter n: "))
list = []
for i in range(n):
    if(i==0 or i ==1):
        list.append(1)
    else:
        fibo = list[i-1] + list[i-2]
        list.append(fibo)
print("fibonanchi is: " , list)