students = int(input("please enter number of students: "))
sum = 0 
mark = []
for i in range(students):
    m = float(input("please enter mark of programming: "))
    mark.append(m)
    sum += m
avg = round(sum / students , 2)
print("avg of students is: ", avg )
print("max mark of programming is: " , max(mark))
print("min mark of programming is: ", min(mark))