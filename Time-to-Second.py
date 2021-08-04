while True:
    hour = input("please enter hour: ")
    minute = input("please enter minute: ")
    second = input("please enter second: ")
    s= int(hour)*3600 + int (minute)*60 + int(second)
    print("time to second is: ", s)