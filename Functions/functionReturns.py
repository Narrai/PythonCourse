def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text

# call the function
# result = center_text("spam and eggs")
# print(result)
# print(center_text("spam, spam, and eggs"))
# print(center_text(12))
# print(center_text("spam, spam, spam, and spam"))
# print(center_text("first", "second", 3, 4, "spam", sep=":"))

with open("center", 'w') as menu:
    result = center_text("spam and eggs")
    print(result, file=menu)
    print(center_text("spam, spam, and eggs"), file=menu)
    print(center_text(12), file=menu)
    print(center_text("spam, spam, spam, and spam"), file=menu)
    print(center_text("first", "second", 3, 4, "spam", sep=":"), file=menu)
