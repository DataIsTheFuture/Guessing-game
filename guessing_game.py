# Let's try to guess if the name you say is into my chosen ones for a category.

color_lst = ["Green", "Blue", "Orange", "Violet", "Red"]
city_lst = ["Madrid", "Lisbon", "Paris", "Rome", "London"]
object_lst = ["Computer", "TV", "Table", "Phone", "Book"]

x = input("Do you want to guess a color, a city, or an object? ")

while x != "color" and x != "city" and x != "object":
    print("This category doesn't exist or is not included yet!")
    x = input("Choose another one: ")

print(f"Ok!, Seems that you want to guess my {x}, let's play!")
y = input(f"What {x} do you choose? ")

if x == "color":
    while y not in color_lst:
        print("Incorrect! Try again")
        y = input(f"What {x} do you choose? ")
elif x == "city":
    while y not in city_lst:
        print("Incorrect! Try again")
        y = input(f"What {x} do you choose? ")
elif x == "object":
    while y not in object_lst:
        print("Incorrect! Try again")
        y = input(f"What {x} do you choose? ")

print("Correct!")
