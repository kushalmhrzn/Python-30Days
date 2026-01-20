#convering integer to float

#interger_number = 123 #We get TypeError, if we try to add str and int. For example, '12' + 23. Python is not able to use Implicit Conversion in such conditions.
#float_number = 13.23

#new_number = interger_number + float_number

#print("Value",new_number)
#print("Type:",type(new_number)) #o prints the type of new_number variable

# addition of integer and string using excplicit conversion
 num_string = '234'
num_integer = 44

print("data type of num_string:",type(num_string))

num_sum = int(num_string)
print("data type of num_sum after conversion:",type(num_sum))

num_sum = num_integer + num_sum

print("sum:",num_sum)

