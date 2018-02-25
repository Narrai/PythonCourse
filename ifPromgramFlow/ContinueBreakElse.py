# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         # continue
#         break
#     print("Buy " + item)

meal = ["egg", "bacon", "bean", "sausages"]

nasty_food_item = ""
for item in meal:
    if item == "spam":
        nasty_food_item = "spam"
        break
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it.")