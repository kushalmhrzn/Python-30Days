print("this is 'kushal'")  #quotes inside quotes

#assing string to a variable
a = 'ram'
print(a)

#multiline string
#it helps to seperate the lines
b = """this is the multiline string
which we can write 
in this way"""
print(b)

#string array

k = "this is kushal maharjan" #this line is string array
print(k[1]) #it will print the seletect number index character
print(k[2])
print(k[3])
print(k[4])
print(k[5])
print(k[6])
print(k[7])
print(k[9])

#looping through a string
for x in 'anana':
    print(x)


#string length
print(len(k))

#check string
##print("freeee" in txt)

#using if
#txt = "The best things in life are free!"
#if "free" in txt:  #we using in keyword to check the string
#    print("yes free is present")

#check if not present
kk = "The best things in life are free!"
if "freeee" not in kk:  #we using not in keyword to check the string
    print("no free is present")


#trying my own

abc = "there is a ball in the canteen"
if "baaall" in abc:
    print("'yes', your are right")
else:
    print("'no', your are wrong")


