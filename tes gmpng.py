print ("  bryan")
print ("\t bryan")
print ("\n\t bryan")

complanguage = '  python   '
print (complanguage.rstrip())
print (complanguage.lstrip())
print (complanguage.strip())

age = 33
message = "Happy " + str(age) + "rd birthday"
print (message)

#LIST ATAU ARRAY DI BAHASA LAIN

laptopmanufactures = ["MSI", "ASUS", "LENOVO", "ACER"]
print (laptopmanufactures)
print (laptopmanufactures[0])
print (laptopmanufactures[2])
print (laptopmanufactures[-1])
print (laptopmanufactures[-2])
print (laptopmanufactures[1:3])
laptopmanufactures[0] = "Apple Sucks"
print (laptopmanufactures)
print (laptopmanufactures[1].title())
laptopmanufactures.append("HP")
print (laptopmanufactures)
laptopmanufactures.insert(1,"Dell")
print (laptopmanufactures)
del laptopmanufactures[2]
print (laptopmanufactures)
print (laptopmanufactures[1:3])

#sort string dan reverse
student_females = ['Misa','Jocelyn','Nico','Aric']
print (student_females)
sorted_student_females = sorted(student_females)
print (sorted_student_females)
student_females.reverse()
print (student_females)
#sort angka
ages = [22,25,90,32]
ages.sort()
print (ages)

#POP
cars = ['honda','toyota','mitsubishi']
popped_cars = cars.pop(1)
print (cars)
print (popped_cars)

#FOR
for student_female in student_females :
    print (student_female)

