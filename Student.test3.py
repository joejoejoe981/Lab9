import csv

from Lab09.Student import Student

with open('students.csv',newline='',encoding='utf-8') as f:
    r = csv.reader(f,delimiter=',')
    for x in r:

        print(x)
        #st = Student(x[0],x[1],x[2])
        st = Student(*x)
        st.show()
