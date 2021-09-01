#TestFile
x= 5
y=x+3
y=int(str(y)+"2")
print(y, "\n")


x=3
num=17
print(num%x, "\n")


i = 0
x = 0
while i < 4:
    x+=i
    i+=1

print(x, "\n")


x = [2, 4]
x += [6, 8]
print(x[2]//x[0], "\n")



list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x % 2 == 1 and x > 4):
        print(x, "\n")
        break


list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]],"\n")


