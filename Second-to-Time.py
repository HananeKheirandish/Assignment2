import math
Second = int(input("please enter second: "))
hour = Second / 3600
minute = (Second % 3600) / 60
second = (Second % 3600) % 60
print(str(int(hour)).zfill(2),":",str(int(minute)).zfill(2),":",str(int(second)).zfill(2))