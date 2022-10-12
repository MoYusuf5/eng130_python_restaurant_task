# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

menu = {
    "starters" : ["spring rolls", "Soup", "Salad"],
    "mains" : ["grilled beef", "fried fish"],
    "desserts" : ["apple crumble", "ice cream", "cheesecake"]
}

print("Do You Want To See Our Menu? yes/no: ")
view_menu = str(input())

if view_menu == "yes":
    print(menu)
    view_menu = str(input("What would you like to order?"))


elif view_menu == "no":
    print("Thanks, Enjoy Your Day!")






