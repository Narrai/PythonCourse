import shelve

# blt = ["bacon", "lettuce", "tomato",  "bread"]
# beans_on_toast = ["beans",  "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # This code can append the value to the list
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # recipes["soup"].append("croutons")

    recipes["soup"] = soup
    recipes.sync()  # the soup list object is not stored in the cache and the sync causes the cache to be cleared on
    soup.append("cream")  # soup.append does add cream to the list but there is no corresponding object in the cache\
# anymore because we called recipes.sync(). So when we loop through the list, actually we are retrieving the lists from
# disk so the list object we are retrieving is not the one that we append the cream
    for snack in recipes:
        print(snack, recipes[snack])
