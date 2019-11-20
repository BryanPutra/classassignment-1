#EXERCISE 3-4 to 3-8 FROM THE BOOK PAGE 46 AND 50

INVITED = ['MOM','DAD','SIS']
print (INVITED)
del INVITED[2]
INVITED.insert(2,"BRO")
print (INVITED)
message_to_mom = str(INVITED[0]) + ", you are invited to my dinner."
message_to_dad = str(INVITED[1]) + ", you are invited to my dinner."
message_to_bro = str(INVITED[2]) + ", you are invited to my dinner."
print (message_to_mom)
print (message_to_bro)
print (message_to_dad)
INVITED.append("AUNT")
INVITED.append("UNCLE")
INVITED.append("COUSIN")
print (INVITED)
message_to_aunt = str(INVITED[3]) + ", you are invited to my dinner."
message_to_uncle = str(INVITED[4]) + ", you are invited to my dinner."
message_to_cousin = str(INVITED[5]) + ", you are invited to my dinner."
print (message_to_mom)
print (message_to_bro)
print (message_to_dad)
print (message_to_aunt)
print (message_to_uncle)
print (message_to_cousin)

print ("ONLY 2 SLOTS AVAILABLE FOR DINNER")
message_remove_to_cousin = str(INVITED[5]) + ", sorry we suddenly have technical problems so now we only have two slots for the dinner."
print (message_remove_to_cousin)
popped_COUSIN = INVITED.pop()
message_remove_to_uncle = str(INVITED[4]) + ", sorry we suddenly have technical problems so now we only have two slots for the dinner."
print (message_remove_to_uncle)
popped_uncle = INVITED.pop()
message_remove_to_aunt = str(INVITED[3]) + ", sorry we suddenly have technical problems so now we only have two slots for the dinner."
print (message_remove_to_aunt)
popped_aunt = INVITED.pop()
message_remove_to_bro = str(INVITED[2]) + ", sorry we suddenly have technical problems so now we only have two slots for the dinner."
print (message_remove_to_bro)
popped_bro = INVITED.pop()

updatemessage_to_mom = str(INVITED[0]) + ", you are still invited even though the slots have decreased"
updatemessage_to_dad = str(INVITED[1]) + ", you are still invited even though the slots have decreased"
print (updatemessage_to_dad)
print (updatemessage_to_mom)

del INVITED[1]
del INVITED[0]
print (INVITED)

# PAGE 50

placeiwannavisit = ['England', 'Australia', 'Japan', 'Germany', 'Indonesia']
print (placeiwannavisit)
sorted_placeiwannavisit = sorted(placeiwannavisit)
print (sorted_placeiwannavisit)
print (placeiwannavisit)
sorted_placeiwannavisit.reverse()
print (sorted_placeiwannavisit)
print (placeiwannavisit)
placeiwannavisit.reverse()
print (placeiwannavisit)
placeiwannavisit.reverse()
print (placeiwannavisit)
placeiwannavisit.sort()
print (placeiwannavisit)
placeiwannavisit.sort(reverse = True)
print (placeiwannavisit)



#1
degrees = 150
print ('Degrees:', degrees)
radians = degrees / 180 * 3.14
print ('Radians:', radians)

#2
student1 = 80
student2 = 90
student3 = 66.5
print (student1)
print (student2)
print (student3)
averagescore = (student2+student3+student1) / 3
print (averagescore)

#3
firstclass = 32
secondclass = 45
thirdclass = 51
firstclassgroups = 5
secondclassgroups  = 7
thirdclassgroups = 6
firstclassgroupmembers = firstclass//firstclassgroups
secondclassgroupmembers = secondclass//secondclassgroups
thirdclassgroupmembers = thirdclass//thirdclassgroups
firstclassleftovers = firstclass%firstclassgroups
secondclassleftovers = secondclass%secondclassgroups
thirdclassleftovers = thirdclass%thirdclassgroups
print (firstclassgroupmembers)
print (secondclassgroupmembers)
print (thirdclassgroupmembers)
print (firstclassleftovers)
print (secondclassleftovers)
print (thirdclassleftovers)

#4
pi = 3.14
piediameter = 55.4
pie_radius = piediameter / 2
print (pie_radius)
circumference = 2 * pi * pie_radius
circumferencemsg = "Jimmy’s pie has a circumference:"
print(circumferencemsg, circumference)

#5
v = 343
f = 256
print ('The speed (m/s):', v)
print ('The frequency (Hz):', f)
Wavelength = v/f
print ('The wavelength (m):', Wavelength)



