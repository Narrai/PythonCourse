import shelve

# blt = ["becon", "lettuce", "tomato",  "bread"]
# beans_on_toast = ["beans",  "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes") as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # UPDATING THE VALUE
    # recipes["blt"].append("butter")  # does not work as it seems that appending while reading
    # recipes["pasta"].append("tomato")

    # This code can append the value to the list
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomata")
    # recipes["pasta"] = temp_list
    for snack in recipes:
        print(snack, recipes[snack])
