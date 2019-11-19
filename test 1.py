print ("Hello World")
var = 20
var_2 = 30
var_3 = "HI"
var_4 = 5.2
var_5 = True
print (type(var_3))
print (type(var_2))
print (type(var_4))
print (type(var_5))

for letter in "python":
    print ("alphabet is",letter)

val = "a"
i = 0
vaal = "B"
star = "*"

while i < 5:
    print (val)
    i += 1

amount = 5
star = "*"
starspace = "* "

for i in range(amount):
    print (star * (i+1))

for i in range(amount):
    print (star * (amount-i))

space = " "
for i in range(amount):
    print (space * (amount - (i+1)) + star * (i+1))

for i in range(amount-1,-1,-1):
    print (space * (amount-i-1) + star * (i+1))

for i in range(amount):
    print (space * (amount-i-1) + starspace * (i+1))
for j in range(amount-1,0,-1):
    print (space * (amount-j) + starspace*j)

diamondrows = 5
n = 0
h = 3
for n in range(h):
    print(" "*(h-n), "*"*(n*2+1))
for n in range(h-2, -1, -1):
    print(" "*(h-n), "*"*(n*2+1))

titles = "the shit"
print (titles.title())
print (titles.upper())
print (titles.lower())