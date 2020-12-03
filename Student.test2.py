from Lab09.Student import Student

#st1 = Student()
st1 = Student('Tom',python = 100,eng = 80,math = 90)
st1.show()

a = ('Tom',80,90,100)
st2 = Student(*a)
st2.show()

a = {'name':'Tom','python':100,'eng':80,'math':90}
st3 = Student(**a)
st3.show()

st4 = Student('Tom',80,90,100)
st4.show()

st5 = Student(name = 'Tom',eng = 80,math = 90)
st5.show()

