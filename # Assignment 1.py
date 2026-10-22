# Assignment 1
# Variables Video 2

'''greeting = "hello world"
fav_num = 7 
num_string = "5"
love_programming = False

print(greeting)
print(fav_num)
print(love_programming)

my_name = "Genesis"'''

# Input and output Video 3

'''username = input("What is your name?")
fav_num = int(input("What is your favourite number?"))
double = fav_num * 2
halve = fav_num / 2
square = fav_num + fav_num

print(f"\nHi{username}, your favourite number is {fav_num}")

print(f"Double {fav_num} is {double}.")
print(f"Half {fav_num} is {halve}.")
print(f"{fav_num} squared is {square}")
print()
print("Have a nice day.")'''

# Get width Video 4

'''error = "Please enter a number that is more than zero\n"
while True:

    try:
        width = float(input("Width: "))

        if width > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)'''

# Number checker Video 5

'''def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            width = float(input(question))

            if width > 0:
                return width
            else:
                print(error)
        except ValueError:
            print(error)

for item in range (0, 2):
    width = num_check("width: ")
    print(width)

print()

for item in range (0, 2):
    height = num_check("Height: ")
    print(height)

# Area perimeter Video 6

width = float(input("Width: "))
height = float(input("Height: "))

area = width * height
perimeter = 2 * (width + height)

print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")'''

# Final Perimeter Calculator
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


keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    area = width * height
    perimeter = 2 * (width + height)

    print ()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    keep_going = input("Press enter to keep going or any key to quit")
    print()

print("Thank you for using the area / perimeter calculator")



