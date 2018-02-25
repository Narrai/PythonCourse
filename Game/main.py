from player import Player
p = Player('Nar')
p.lives = 10
p.score = 5
p.level = 8
print(p)
# from enemy import Enemy, Troll, Vampire, VampireKing
#
# dracula = VampireKing("Dracula")
# print(dracula)
# dracula.take_damage(12)
# print(dracula)

# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
# another_troll.take_damage(18)
# print(another_troll)
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp = Vampire("Vlad")
# print(vamp)
#
# vamp.take_damage(5)
# print(vamp)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
# while vamp._alive:
#     vamp.take_damage(1)
