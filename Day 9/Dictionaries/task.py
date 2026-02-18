programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Add element to dictionary

programming_dictionary["Loop"] = "Something"
print(programming_dictionary)

# Edit an element

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wipe the dictionary

programming_dictionary = {}
print(programming_dictionary)