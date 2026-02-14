bmi = 84 / 1.65 ** 2
print(bmi)

# Similar to using floor
print(int(bmi))

# This is the more conventional rounding function
print(round(bmi))

# round() function has a second parameter, which is the numer of integer places it will show at max
# This will also round off the last decimal digit as well
print(round(bmi, 2))