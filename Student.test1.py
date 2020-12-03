#裝箱
a = ('Tom',100,95)
print(a)

#拆箱
name = a[0]
eng = a[1]
math = a[2]
print(name,math,eng)

#自動拆箱
name,eng,math = a
print(name,eng,math)
