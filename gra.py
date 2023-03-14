import blucachka

fointain = blucachka.Park("Фонтан")
fointain.set_description("Красивий фонтан у центрі парку.")

ozero = blucachka.Park("Озеро")
ozero.set_description("Велике озеро з качками і лебедями.")

lavka = blucachka.Park("Лавочка")
lavka.set_description("Самотня дерев'яна лавочка біля стежки.")

fointain.link_location(ozero, "вниз")
ozero.link_location(fointain, "вгору")
ozero.link_location(lavka, "ліворуч")
lavka.link_location(ozero, "праворуч")

lotr = blucachka.Enemy("Лотр", "Розбійник")
lotr.set_conversation("Чого прийшли сюди!?")
lotr.set_weakness("шокер")
lavka.set_character(lotr)

gypsy = blucachka.Enemy("Циганка", "Стара циганка без грошей.")
gypsy.set_conversation("Дайте на хліб...")
gypsy.set_weakness("гроші")
fointain.set_character(gypsy)

bilka = blucachka.Enemy("Білка", "Маленька білочка")
bilka.set_conversation("Хочу горішків...")
bilka.set_weakness("9 горішків")
ozero.set_character(bilka)

shoker = blucachka.Item("шокер")
shoker.set_description("шокер щоб лякати лотрів")
fointain.set_item(shoker)

money = blucachka.Item("гроші")
money.set_description("гроші для циганки")
ozero.set_item(money)

nuts = blucachka.Item("горішки")
nuts.set_description("3 смачних горішки для білочки")
lavka.set_item(nuts)
ozero.set_item(nuts)
fointain.set_item(nuts)

angel = blucachka.Friend("друг")
angel.set_description("Допоможу своїми горішками перемогти білочку")
ozero.set_friend(angel)
lavka.set_friend(angel)
fointain.set_friend(angel)

current_room = fointain
backpack = []
dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["вниз", "вгору", "праворуч", "ліворуч"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "розмова":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "битва":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("З чим будете битися?")
            fight_with = input()

            if inhabitant == bilka:

                # Do I have this item?
                if fight_with in backpack:
                    if backpack.count(fight_with) == 3:

                        if inhabitant.fight(fight_with) == True:
                            # What happens if you win?
                            print("Урааа, ви перемогли у цьому поєдинку!")
                            current_room.character = None
                            if inhabitant.get_defeated() == 3:
                                print("Мої вітання, у вас вийшло вийти неушкодженим!")
                                dead = True
                        else:
                            # What happens if you lose?
                            print("На жаль, ви програли у цій грі.")
                            print("Це кінець гри.")
                            dead = True
                else:
                    print("У вас немає достатньо " + fight_with)
                    print(help(angel))
                    backpack.append("горішки")
                    backpack.append("горішки")
            else:
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Урааа, ви перемогли у цьому поєдинку!")
                        current_room.character = None
                        if inhabitant.get_defeated() == 2:
                            print("Мої вітання, у вас вийшло вийти неушкодженим!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("На жаль, ви програли у цій грі.")
                        print("Це кінець гри.")
                        dead = True
                else:
                    print("У вас немає " + fight_with)        
        else:
            print("Тут немає з ким битись")
    elif command == "взяти":
        if item is not None:
            print("Ви поставили " + item.get_name() + " у свою кишеню")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Тут нічого немає!")
    else:
        print("Ви не можете " + command)
