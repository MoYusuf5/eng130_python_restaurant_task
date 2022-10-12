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
    order_list = []

    order_1 = input("Please make your first order")
    order_list.append(order_1)

    order_2 = input("Please make your second order")
    order_list.append(order_2)

    order_3 = input("Please make your third order")
    order_list.append(order_3)

    for a in order_list:
        print(a)
elif view_menu == "no":
    print("Thanks, Enjoy Your Day!")








