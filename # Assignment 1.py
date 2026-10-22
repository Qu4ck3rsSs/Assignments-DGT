# Assignment 1

# Final Perimeter Calculator
# This is a function that checks for a valid number
def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            value = float(input(question))

            if value > 0:
                return value
            else:
                print(error)
        except ValueError:
            print(error)

# This function helps calculate the height and width of a valid number after it checks it can be used 
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    area = width * height
    perimeter = 2 * (width + height)

    print ()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

# This function allows the user to keep going after the program has finished or let them completely stop the program
    keep_going = input("Press enter to keep going or any key to quit")
    print()

# This is a goodbye message
print("Thank you for using the area / perimeter calculator")



