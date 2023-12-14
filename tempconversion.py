#!bin/python3
temp_f = input('Enter temperature in fahrenheit: ')
temp_c =  5/9 * (float(temp_f) - 32)
print('your temperature in celsius is:', temp_c)
if temp_c > 30:
    print("It's hot af\ndrink plenty of water")
else:
    print("Not that hot honestly")
