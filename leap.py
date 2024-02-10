# Making a Leap Year Program
# Welcome Message
print("A leap year coding project in python by: Maiwand safi")

# Creating the first year variable to hold the data.
year = int(input("Enter the year: "))

# we will create the logic for the leap year.
if year % 4 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Leap Year")
elif year % 400 == 0:
    print("Leap Year")
else:
    print("It's not the leap year")
