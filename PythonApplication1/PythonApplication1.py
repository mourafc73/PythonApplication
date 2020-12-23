# Create a variables
height = 1.82
weight = 78
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

BMI = weight / height **2
print (BMI)
print(type(BMI))


# Calculate result
result = (savings * growth_multiplier ** 7)

# Print out result
print (result)

# Assign product of growth_multiplier and savings to year1
year1 = savings * growth_multiplier

# Print the type of year1
print (year1)

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print (doubledesc)

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)