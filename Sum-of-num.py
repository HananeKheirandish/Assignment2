sum = 0
while True :
    x = input("please enter numbers: ")
    if (x == "exit"):
        break
    else:
        sum += float(x)
print("sum of your numbers is " , sum )