integer_number = int(input("Enter the Integer Number:"))
float_number = float(input("Enter the Float number:"))

#converting implict conversion

result = integer_number + float_number

print(result)
print(type(result))


#explicit conversion

number_1 = 22
number_2 = 33.21

print("data types of num_string before type casting:",type(number_1))

#explict conversion
number_1 = float(number_1)

print("data types of num_string after type casting:",type(number_1))

num_sum = number_1 + number_2
print(num_sum)

