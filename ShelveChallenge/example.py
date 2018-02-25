import shelve

# books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
#                      "beans_on_toast": ["beans", "bread"],
#                      "scrambled eggs": ["eggs", "butter", "milk"],
#                      "soup": ["tin of soup"],
#                      "pasta": ["pasta", "cheese"]},
#          "maintenance": {"stuck": ["oil"],
#                          "loose": ["gaffer tape"]}}
# print(books["recipes"]["soup"])
# print(books["recipes"]["pasta"])
#
# print(books["maintenance"]["loose"])

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}
print(books["recipes"]["soup"])
print("*" * 40)
print((books["maintenance"]["stuck"]))
