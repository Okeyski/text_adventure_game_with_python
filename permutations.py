import sys, time
import config


level_one = config.level_one
level_two = config.level_two
level_three = config.level_three


def end():
    sys.exit("You're out of options and still trapped. Mission Failed")


# loops through the dictionary
def level():
    global level_one
    for i in level_one:
        print(i, level_one[i], sep=". ")


def level2():
    global level_two
    for i in level_two:
        print(i, level_two[i], sep=". ")


def level3():
    global level_three
    for i in level_three:
        print(i, level_three[i], sep=". ")


def option():
    enter = input("Select option: ")
    return enter


# makes the print function print slower
def sprint(str):
    for letter in str + "\n":
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.09)


# permutations for the first level
def first():
    global level_one
    pot = (
        {}
    )  # To store user input in the format: "option-picked"_pick_"position-picked"
    if "1" not in level_one:
        while True:
            level()
            text = option()
            if text not in ["2", "3", "1"]:
                print("invalid entry")
                continue
            if text not in level_one:
                print("Option no longer accessible")  # blocks possible loopholes
                continue
            if text == "2":
                del level_one["2"]
                if "3_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You set the wooden bar on fire. It burns easily exposing the charred lock handle.\n"
                    )
                    end()
                else:
                    pot["2_pick_1"] = None
                    sprint(
                        "You set the wooden bar on fire. It burns easily exposing the charred lock handle.\n"
                    )
                    continue
            else:
                del level_one["3"]
                if "2_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint("With a mighty swing, you break the lock \nSUCCESS!\n")
                    return
                else:
                    pot["3_pick_1"] = None
                    sprint(
                        "With a mighty swing, you hit the wooden bar... and your axe breaks. Bummer\n"
                    )
                    continue
    elif "2" not in level_one or "3" not in level_one:
        while True:
            level()
            text = option()
            if text not in ["1", "2", "3"]:
                print("invalid entry")
                continue
            if text not in level_one:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_one["1"]
                sprint("You spray the wooden bar with the smelly liquid.\n")
            if text == "3":
                del level_one["3"]
                sprint(
                    "With a mighty swing, you hit the wooden bar... and your axe breaks. Bummer\n"
                )
            if text == "2":
                del level_one["2"]
                sprint("You try to set the wooden bar on fire but it doesn’t catch.\n")
            if len(level_one) == 0:
                end()


# permutations for the second level
def second():
    global level_two
    pot = {}
    if "1" not in level_two:
        while True:
            level2()
            text = option()
            if text not in ["1", "2", "3", "4"]:
                print("invalid entry")
                continue
            if text not in level_two:
                print("Option no longer accessible")
                continue
            if text == "2":
                del level_two["2"]
                if "3_pick_1" in pot and "4_pick_2" in pot:
                    pot["2_pick_3"] = None
                    sprint(
                        "You quickly activate the decoy which distracts the surprised guard as he moves to attack what he thinks is you.\n"
                    )
                    end()
                elif "3_pick_2" in pot and "4_pick_1" in pot:
                    pot["2_pick_3"] = None
                    sprint(
                        "You put on the mask but the dog is not fooled. You carry an unfamiliar scent.\n"
                    )
                    end()
                elif "3_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You put on the mask but the dog is not fooled. You carry an unfamiliar scent.\n"
                    )
                elif "4_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You put on the mask… And now you look like one of the guards. The effects don’t last long.\n"
                    )
                else:
                    pot["2_pick_1"] = None
                    sprint(
                        "You put on the mask… And now you look like one of the guards. The effects don’t last long.\n"
                    )
            elif text == "3":
                del level_two["3"]
                if ("2_pick_1" in pot and "4_pick_2" in pot) or (
                    "2_pick_2" in pot and "4_pick_1" in pot
                ):
                    pot["3_pick_3"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
                    end()
                elif "2_pick_1" in pot or "4_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
                else:
                    pot["3_pick_1"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
            elif text == "4":
                del level_two["4"]
                if ("3_pick_1" in pot and "2_pick_2" in pot) or (
                    "3_pick_2" in pot and "2_pick_1" in pot
                ):
                    pot["4_pick_3"] = None
                    sprint(
                        "You throw the ‘bone’ at the dog and it jumps to catch it.\nThe enchantment disintegrates the dog and causes a loud alarm!\nYou quickly pick up the dog’s tag seconds before a scary guard walks into the room.\nHe points his spear at you.\n"
                    )
                    end()
                elif "3_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You throw the ‘bone’ at the dog and it jumps to catch it.\nThe enchantment disintegrates the dog and causes a loud alarm!\nYou quickly pick up the dog’s tag seconds before a scary guard walks into the room.\nHe points his spear at you.\n"
                    )
                elif "2_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You inspect the bone wondering what the witches would need an enchanted bone for.\n"
                    )
                else:
                    pot["4_pick_1"] = None
                    sprint(
                        "You inspect the bone wondering what the witches would need an enchanted bone for.\n"
                    )
    elif "2" not in level_two:
        while True:
            level2()
            text = option()
            if text not in ["1", "2", "3", "4"]:
                print("invalid entry")
                continue
            if text not in level_two:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_two["1"]
                if "3_pick_1" in pot and "4_pick_2" in pot:
                    pot["1_pick_3"] = None
                    sprint(
                        "You quickly activate the decoy which distracts the surprised guard as he moves to attack what he thinks is you.\n"
                    )
                    end()
                elif "3_pick_2" in pot and "4_pick_1" in pot:
                    pot["1_pick_3"] = None
                    sprint(
                        "You quickly activate the decoy but the dog is not fooled. It can smell the real you.\n"
                    )
                    end()
                elif "3_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You quickly activate the decoy but the dog is not fooled. It can smell the real you.\n"
                    )
                elif "4_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You activate the decoy and are marveled by its effects which don’t last long.\n"
                    )
                else:
                    pot["1_pick_1"] = None
                    sprint(
                        "You activate the decoy and are marveled by its effects which don’t last long.\n"
                    )
            elif text == "3":
                del level_two["3"]
                if ("1_pick_1" in pot and "4_pick_2" in pot) or (
                    "1_pick_2" in pot and "4_pick_1" in pot
                ):
                    pot["3_pick_3"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
                    end()
                elif "1_pick_1" in pot or "4_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
                else:
                    pot["3_pick_1"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
            elif text == "4":
                del level_two["4"]
                if ("3_pick_1" in pot and "1_pick_2" in pot) or (
                    "3_pick_2" in pot and "1_pick_1" in pot
                ):
                    pot["4_pick_3"] = None
                    sprint(
                        "You throw the ‘bone’ at the dog and it jumps to catch it.\nThe enchantment disintegrates the dog and causes a loud alarm!\nYou quickly pick up the dog’s tag seconds before a scary guard walks into the room.\nHe points his spear at you.\n"
                    )
                    end()
                elif "3_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You throw the ‘bone’ at the dog and it jumps to catch it.\nThe enchantment disintegrates the dog and causes a loud alarm!\nYou quickly pick up the dog’s tag seconds before a scary guard walks into the room.\nHe points his spear at you.\n"
                    )
                elif "1_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You inspect the bone wondering what the witches would need an enchanted bone for.\n"
                    )
                else:
                    pot["4_pick_1"] = None
                    sprint(
                        "You inspect the bone wondering what the witches would need an enchanted bone for.\n"
                    )

    elif "3" not in level_two:
        while True:
            level2()
            text = option()
            if text not in ["1", "2", "3", "4"]:
                print("invalid entry")
                continue
            if text not in level_two:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_two["1"]
                if "2_pick_1" in pot and "4_pick_2" in pot:
                    pot["1_pick_3"] = None
                    sprint(
                        "You quickly activate the decoy which distracts the surprised guard as he moves to attack what he thinks is you.\n"
                    )
                    end()
                elif "2_pick_2" in pot and "4_pick_1" in pot:
                    pot["1_pick_3"] = None
                    sprint(
                        "You quickly activate the decoy which distracts the surprised guard as he moves to attack what he thinks is you.\n"
                    )
                    end()
                elif "2_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You activate the decoy and are marveled by its effects which don’t last long.\n"
                    )
                elif "4_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You quickly activate the decoy which distracts the surprised guard as he moves to attack what he thinks is you.\n"
                    )
                else:
                    pot["1_pick_1"] = None
                    sprint(
                        "You quickly activate the decoy but the dog is not fooled. It can smell the real you.\n"
                    )
            elif text == "2":
                del level_two["2"]
                if "1_pick_1" in pot and "4_pick_2" in pot:
                    pot["2_pick_3"] = None
                    sprint("The guard sees you putting on the mask. A wasted effort.\n")
                    end()
                elif "1_pick_2" in pot and "4_pick_1" in pot:
                    pot["2_pick_3"] = None
                    sprint(
                        "You put on the mask just as the decoy fades and using the enchanted tag, walk out of the room with the guard oblivious.\nSUCCESS!\n"
                    )
                    return
                elif "1_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You put on the mask but the dog is not fooled. You carry an unfamiliar scent.\n"
                    )
                elif "4_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint("The guard sees you putting on the mask. A wasted effort.\n")
                else:
                    pot["2_pick_1"] = None
                    sprint(
                        "You put on the mask but the dog is not fooled. You carry an unfamiliar scent.\n"
                    )
            elif text == "4":
                del level_two["4"]
                if ("2_pick_1" in pot and "1_pick_2" in pot) or (
                    "2_pick_2" in pot and "1_pick_1" in pot
                ):
                    pot["4_pick_3"] = None
                    sprint(
                        "You throw the ‘bone’ at the dog and it jumps to catch it.\nThe enchantment disintegrates the dog and causes a loud alarm!\nYou quickly pick up the dog’s tag seconds before a scary guard walks into the room.\nHe points his spear at you.\n"
                    )
                    end()
                elif "2_pick_1" in pot or "1_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You throw the ‘bone’ at the dog and it jumps to catch it.\nThe enchantment disintegrates the dog and causes a loud alarm!\nYou quickly pick up the dog’s tag seconds before a scary guard walks into the room.\nHe points his spear at you.\n"
                    )
                else:
                    pot["4_pick_1"] = None
                    sprint(
                        "You throw the ‘bone’ at the dog and it jumps to catch it.\nThe enchantment disintegrates the dog and causes a loud alarm!\nYou quickly pick up the dog’s tag seconds before a scary guard walks into the room.\nHe points his spear at you.\n"
                    )

    else:
        while True:
            level2()
            text = option()
            if text not in ["1", "2", "3", "4"]:
                print("invalid entry")
                continue
            if text not in level_two:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_two["1"]
                if ("3_pick_1" in pot and "2_pick_2" in pot) or (
                    "3_pick_2" in pot and "2_pick_1" in pot
                ):
                    pot["1_pick_3"] = None
                    sprint(
                        "You quickly activate the decoy but the dog is not fooled. It can smell the real you.\n"
                    )
                    end()
                elif "3_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You quickly activate the decoy but the dog is not fooled. It can smell the real you.\n"
                    )
                elif "2_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You activate the decoy and are marveled by its effects which don’t last long.\n"
                    )
                else:
                    pot["1_pick_1"] = None
                    sprint(
                        "You activate the decoy and are marveled by its effects which don’t last long.\n"
                    )
            elif text == "3":
                del level_two["3"]
                if ("1_pick_1" in pot and "2_pick_2" in pot) or (
                    "1_pick_2" in pot and "2_pick_1" in pot
                ):
                    pot["3_pick_3"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
                    end()
                elif "1_pick_1" in pot or "2_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
                else:
                    pot["3_pick_1"] = None
                    sprint(
                        "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you.\n"
                    )
            elif text == "2":
                del level_two["2"]
                if ("3_pick_1" in pot and "1_pick_2" in pot) or (
                    "3_pick_2" in pot and "1_pick_1" in pot
                ):
                    pot["2_pick_3"] = None
                    sprint(
                        "You put on the mask but the dog is not fooled. You carry an unfamiliar scent.\n"
                    )
                    end()
                elif "3_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You put on the mask but the dog is not fooled. You carry an unfamiliar scent.\n"
                    )
                elif "1_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You put on the mask… And now you look like one of the guards. The effects don’t last long.\n"
                    )
                else:
                    pot["2_pick_1"] = None
                    sprint(
                        "You put on the mask… And now you look like one of the guards. The effects don’t last long.\n"
                    )


# permutations for final level
def third():
    global level_three
    pot = {}
    if "1" not in level_three:
        while True:
            level3()
            text = option()
            if text not in ["1", "2", "3", "4", "5"]:
                print("invalid entry")
                continue
            if text not in level_three:
                print("Option no longer accessible")
                continue
            if text == "2":
                del level_three["2"]
                sprint(
                    "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                )
            elif text == "3":
                del level_three["3"]
                sprint("You attempt to lubricate the lever but it’s already damaged.\n")
            elif text == "4":
                del level_three["4"]
                sprint("You forcefully try to remove the mirror and it breaks.\n")
            elif text == "5":
                del level_three["5"]
                sprint(
                    "You step on the switch and the grate opens.\n It stays open for a minute and shuts.\n"
                )
            if len(level_three) == 0:
                end()
    elif "2" not in level_three:
        while True:
            level3()
            text = option()
            if text not in ["1", "2", "3", "4", "5"]:
                print("invalid entry")
                continue
            if text not in level_three:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_three["1"]
                if (
                    ("3_pick_1" in pot and "4_pick_2" in pot and "5_pick_3" in pot)
                    or ("3_pick_1" in pot and "4_pick_3" in pot and "5_pick_2" in pot)
                    or ("3_pick_2" in pot and "4_pick_1" in pot and "5_pick_3" in pot)
                    or ("3_pick_2" in pot and "4_pick_3" in pot and "5_pick_1" in pot)
                    or ("3_pick_3" in pot and "4_pick_1" in pot and "5_pick_2" in pot)
                    or ("3_pick_3" in pot and "4_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["1_pick_4"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                    end()
                elif (
                    ("3_pick_1" in pot and "4_pick_2" in pot)
                    or ("3_pick_1" in pot and "5_pick_2" in pot)
                    or ("4_pick_1" in pot and "3_pick_2" in pot)
                    or ("5_pick_1" in pot and "3_pick_2" in pot)
                ):
                    pot["1_pick_3"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                elif "3_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                elif "4_pick_1" in pot or "5_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint("You forcefully try to pull the lever and it breaks.")
                else:
                    pot["1_pick_1"] = None
                    sprint("You forcefully try to pull the lever and it breaks.\n")
            elif text == "3":
                del level_three["3"]
                if (
                    ("1_pick_1" in pot and "4_pick_2" in pot and "5_pick_3" in pot)
                    or ("1_pick_1" in pot and "4_pick_3" in pot and "5_pick_2" in pot)
                    or ("1_pick_2" in pot and "4_pick_1" in pot and "5_pick_3" in pot)
                    or ("1_pick_2" in pot and "4_pick_3" in pot and "5_pick_1" in pot)
                    or ("1_pick_3" in pot and "4_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_3" in pot and "4_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["3_pick_4"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                    end()
                elif ("4_pick_1" in pot and "5_pick_2" in pot) or (
                    "5_pick_1" in pot and "4_pick_2" in pot
                ):
                    pot["3_pick_3"] = None
                    sprint(
                        "You apply the lubricant on the lever and it becomes functional.\n"
                    )
                elif (
                    ("1_pick_1" in pot and "4_pick_2" in pot)
                    or ("1_pick_1" in pot and "5_pick_2" in pot)
                    or ("4_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "1_pick_2" in pot)
                ):
                    pot["3_pick_3"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                elif "4_pick_1" in pot or "5_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "You apply the lubricant on the lever and it becomes functional.\n"
                    )
                elif "1_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                else:
                    pot["3_pick_1"] = None
                    sprint(
                        "You apply the lubricant on the lever and it becomes functional.\n"
                    )
            elif text == "4":
                del level_three["4"]
                if (
                    ("1_pick_2" in pot and "3_pick_1" in pot and "5_pick_3" in pot)
                    or ("1_pick_3" in pot and "3_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_3" in pot and "3_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["4_pick_4"] = None
                    sprint(
                        "You try to align the mirror in front of the energy beam but the beam zaps you when you come close.\n"
                    )
                    end()
                elif (
                    ("1_pick_1" in pot and "3_pick_2" in pot and "5_pick_3" in pot)
                    or ("1_pick_1" in pot and "3_pick_3" in pot and "5_pick_2" in pot)
                    or ("1_pick_2" in pot and "3_pick_3" in pot and "5_pick_1" in pot)
                ):
                    pot["4_pick_4"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
                    end()
                elif "3_pick_1" in pot and "1_pick_2" in pot:
                    pot["4_pick_3"] = None
                    sprint(
                        "You try to align the mirror in front of the energy beam but the beam zaps you when you come close.\n"
                    )
                elif (
                    ("1_pick_1" in pot and "3_pick_2" in pot)
                    or ("1_pick_1" in pot and "5_pick_2" in pot)
                    or ("3_pick_1" in pot and "5_pick_2" in pot)
                    or ("5_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "3_pick_2" in pot)
                ):
                    pot["4_pick_3"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
                elif "1_pick_1" in pot or "3_pick_1" in pot or "5_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
                else:
                    pot["4_pick_1"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
            else:
                del level_three["5"]
                if (
                    ("1_pick_2" in pot and "3_pick_1" in pot and "4_pick_3" in pot)
                    or ("1_pick_3" in pot and "3_pick_1" in pot and "4_pick_2" in pot)
                    or ("1_pick_3" in pot and "3_pick_2" in pot and "4_pick_1" in pot)
                ):
                    pot["5_pick_4"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the energy beam blocks your path to the ladder.\n"
                    )
                    end()
                elif (
                    ("1_pick_1" in pot and "3_pick_2" in pot and "4_pick_3" in pot)
                    or ("1_pick_1" in pot and "3_pick_3" in pot and "4_pick_2" in pot)
                    or ("1_pick_2" in pot and "3_pick_3" in pot and "4_pick_1" in pot)
                ):
                    pot["5_pick_4"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                    end()
                elif "3_pick_1" in pot and "1_pick_2" in pot:
                    pot["5_pick_3"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the energy beam blocks your path to the ladder.\n"
                    )
                elif (
                    ("1_pick_1" in pot and "3_pick_2" in pot)
                    or ("1_pick_1" in pot and "4_pick_2" in pot)
                    or ("3_pick_1" in pot and "4_pick_2" in pot)
                    or ("4_pick_1" in pot and "1_pick_2" in pot)
                    or ("4_pick_1" in pot and "3_pick_2" in pot)
                ):
                    pot["5_pick_3"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                elif "1_pick_1" in pot or "3_pick_1" in pot or "4_pick_1" in pot:
                    pot["5_pick_2"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                else:
                    pot["5_pick_1"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )

    elif "3" not in level_three:
        while True:
            level3()
            text = option()
            if text not in ["1", "2", "3", "4", "5"]:
                print("invalid entry")
                continue
            if text not in level_three:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_three["1"]
                if (
                    ("2_pick_1" in pot and "4_pick_2" in pot and "5_pick_3" in pot)
                    or ("2_pick_1" in pot and "4_pick_3" in pot and "5_pick_2" in pot)
                    or ("2_pick_2" in pot and "4_pick_1" in pot and "5_pick_3" in pot)
                    or ("2_pick_2" in pot and "4_pick_3" in pot and "5_pick_1" in pot)
                    or ("2_pick_3" in pot and "4_pick_1" in pot and "5_pick_2" in pot)
                    or ("2_pick_3" in pot and "4_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["1_pick_4"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                    end()
                elif (
                    ("2_pick_1" in pot and "4_pick_2" in pot)
                    or ("2_pick_1" in pot and "5_pick_2" in pot)
                    or ("4_pick_1" in pot and "2_pick_2" in pot)
                    or ("4_pick_1" in pot and "5_pick_2" in pot)
                    or ("5_pick_1" in pot and "2_pick_2" in pot)
                    or ("5_pick_1" in pot and "4_pick_2" in pot)
                ):
                    pot["1_pick_3"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                elif "2_pick_1" in pot or "4_pick_1" in pot or "5_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                else:
                    pot["1_pick_1"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
            elif text == "2":
                del level_three["2"]
                if (
                    ("1_pick_2" in pot and "4_pick_1" in pot and "5_pick_3" in pot)
                    or ("1_pick_3" in pot and "4_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_3" in pot and "4_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["2_pick_4"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                    end()
                elif (
                    ("1_pick_1" in pot and "4_pick_2" in pot and "5_pick_3" in pot)
                    or ("1_pick_1" in pot and "4_pick_3" in pot and "5_pick_2" in pot)
                    or ("1_pick_2" in pot and "4_pick_3" in pot and "5_pick_1" in pot)
                ):
                    pot["2_pick_4"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out. The mirror redirects it towards the guards. The guards can no longer move.\n"
                    )
                    end()
                elif "1_pick_1" in pot and "4_pick_2" in pot:
                    pot["2_pick_3"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out. The mirror redirects it towards the guards. The guards can no longer move.\n"
                    )
                elif (
                    ("1_pick_1" in pot and "5_pick_2" in pot)
                    or ("4_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "4_pick_2" in pot)
                    or ("4_pick_1" in pot and "5_pick_2" in pot)
                ):
                    pot["2_pick_3"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                elif "1_pick_1" in pot or "4_pick_1" in pot or "5_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                else:
                    pot["2_pick_1"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
            elif text == "4":
                del level_three["4"]
                if (
                    ("1_pick_1" in pot and "2_pick_2" in pot and "5_pick_3" in pot)
                    or ("1_pick_1" in pot and "2_pick_3" in pot and "5_pick_2" in pot)
                    or ("1_pick_2" in pot and "2_pick_1" in pot and "5_pick_3" in pot)
                    or ("1_pick_2" in pot and "2_pick_3" in pot and "5_pick_1" in pot)
                    or ("1_pick_3" in pot and "2_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_3" in pot and "2_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["4_pick_4"] = None
                    sprint(
                        "You try to align the mirror in front of the energy beam but the beam zaps you when you come close.\n"
                    )
                    end()
                elif (
                    ("2_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "1_pick_2" in pot)
                    or ("1_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot)
                ):
                    pot["4_pick_3"] = None
                    sprint(
                        "You try to align the mirror in front of the energy beam but the beam zaps you when you come close.\n"
                    )
                elif ("2_pick_1" in pot and "5_pick_2" in pot) or (
                    "5_pick_1" in pot and "2_pick_2" in pot
                ):
                    pot["4_pick_3"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks."
                    )
                elif "2_pick_1" in pot or "5_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
                elif "1_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You take the mirror and align it at a specific position right in front of the wall switch.\n"
                    )
                else:
                    pot["4_pick_1"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
            else:
                del level_three["5"]
                if (
                    ("1_pick_2" in pot and "2_pick_1" in pot and "4_pick_3" in pot)
                    or ("1_pick_3" in pot and "2_pick_1" in pot and "4_pick_2" in pot)
                    or ("1_pick_3" in pot and "2_pick_2" in pot and "4_pick_1" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot and "4_pick_3" in pot)
                    or ("1_pick_2" in pot and "2_pick_3" in pot and "4_pick_1" in pot)
                ):
                    pot["5_pick_4"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the energy beam blocks your path to the ladder.\n"
                    )
                    end()
                elif "1_pick_1" in pot and "2_pick_3" in pot and "4_pick_2" in pot:
                    pot["5_pick_4"] = None
                    sprint(
                        "You step on the switch and the grate opens. You hurry up the ladder and exit past the open grate with the guards helpless to stop you.\nSUCCESS!\n"
                    )
                    return
                elif (
                    ("2_pick_1" in pot and "1_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot)
                    or ("4_pick_1" in pot and "1_pick_2" in pot)
                ):
                    pot["5_pick_3"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the energy beam blocks your path to the ladder.\n"
                    )
                elif ("2_pick_1" in pot and "4_pick_2" in pot) or (
                    "4_pick_1" in pot and "2_pick_2" in pot
                ):
                    pot["5_pick_3"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                elif "1_pick_1" in pot and "4_pick_2" in pot:
                    pot["5_pick_3"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the guards intercept you before you can get to the ladder.\n"
                    )
                    sys.exit("You've been caught. Mission Failed.")
                elif "2_pick_1" in pot or "4_pick_1" in pot:
                    pot["5_pick_2"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                elif "1_pick_1" in pot:
                    pot["5_pick_2"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the guards intercept you before you can get to the ladder.\n"
                    )
                    sys.exit("You've been caught. Mission Failed.")
                else:
                    pot["5_pick_1"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
    elif "4" not in level_three:
        while True:
            level3()
            text = option()
            if text not in ["1", "2", "3", "4", "5"]:
                print("invalid entry")
                continue
            if text not in level_three:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_three["1"]
                if (
                    ("2_pick_1" in pot and "3_pick_2" in pot and "5_pick_3" in pot)
                    or ("2_pick_1" in pot and "3_pick_3" in pot and "5_pick_2" in pot)
                    or ("2_pick_2" in pot and "3_pick_1" in pot and "5_pick_3" in pot)
                    or ("2_pick_2" in pot and "3_pick_3" in pot and "5_pick_1" in pot)
                    or ("2_pick_3" in pot and "3_pick_1" in pot and "5_pick_2" in pot)
                    or ("2_pick_3" in pot and "3_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["1_pick_4"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                    end()
                elif (
                    ("3_pick_1" in pot and "2_pick_2" in pot)
                    or ("3_pick_1" in pot and "5_pick_2" in pot)
                    or ("2_pick_1" in pot and "3_pick_2" in pot)
                    or ("5_pick_1" in pot and "3_pick_2" in pot)
                ):
                    pot["1_pick_3"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                elif ("2_pick_1" in pot and "5_pick_2" in pot) or (
                    "5_pick_1" in pot and "2_pick_2" in pot
                ):
                    pot["1_pick_3"] = None
                    sprint("You forcefully try to pull the lever and it breaks.\n")
                elif "2_pick_1" in pot or "5_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint("You forcefully try to pull the lever and it breaks.\n")
                elif "3_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                else:
                    pot["1_pick_1"] = None
                    sprint("You forcefully try to pull the lever and it breaks.\n")
            elif text == "2":
                del level_three["2"]
                if (
                    ("1_pick_2" in pot and "3_pick_1" in pot and "5_pick_3" in pot)
                    or ("1_pick_3" in pot and "3_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_3" in pot and "3_pick_2" in pot and "5_pick_1" in pot)
                    or ("1_pick_1" in pot and "3_pick_2" in pot and "5_pick_3" in pot)
                    or ("1_pick_1" in pot and "3_pick_3" in pot and "5_pick_2" in pot)
                    or ("1_pick_2" in pot and "3_pick_3" in pot and "5_pick_1" in pot)
                ):
                    pot["2_pick_4"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                    end()
                elif (
                    ("1_pick_1" in pot and "3_pick_2" in pot)
                    or ("1_pick_1" in pot and "5_pick_2" in pot)
                    or ("3_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "3_pick_2" in pot)
                    or ("3_pick_1" in pot and "5_pick_2" in pot)
                ):
                    pot["2_pick_3"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                elif "1_pick_1" in pot or "3_pick_1" in pot or "5_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                else:
                    pot["2_pick_1"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
            elif text == "3":
                del level_three["3"]
                if (
                    ("1_pick_1" in pot and "2_pick_2" in pot and "5_pick_3" in pot)
                    or ("1_pick_1" in pot and "2_pick_3" in pot and "5_pick_2" in pot)
                    or ("1_pick_2" in pot and "2_pick_1" in pot and "5_pick_3" in pot)
                    or ("1_pick_2" in pot and "2_pick_3" in pot and "5_pick_1" in pot)
                    or ("1_pick_3" in pot and "2_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_3" in pot and "2_pick_2" in pot and "5_pick_1" in pot)
                ):
                    pot["3_pick_4"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                    end()
                elif (
                    ("2_pick_1" in pot and "1_pick_2" in pot)
                    or ("5_pick_1" in pot and "1_pick_2" in pot)
                    or ("1_pick_1" in pot and "5_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot)
                    or ("2_pick_1" in pot and "5_pick_2" in pot)
                    or ("5_pick_1" in pot and "2_pick_2" in pot)
                ):
                    pot["3_pick_3"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                elif "2_pick_1" in pot or "5_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "You apply the lubricant on the lever and it becomes functional.\n"
                    )
                elif "1_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                else:
                    pot["3_pick_1"] = None
                    sprint(
                        "You apply the lubricant on the lever and it becomes functional"
                    )
            else:
                del level_three["5"]
                if (
                    ("1_pick_3" in pot and "2_pick_1" in pot and "3_pick_2" in pot)
                    or ("1_pick_3" in pot and "2_pick_2" in pot and "3_pick_1" in pot)
                    or ("1_pick_2" in pot and "2_pick_3" in pot and "3_pick_1" in pot)
                ):
                    pot["5_pick_4"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the energy beam blocks your path to the ladder.\n"
                    )
                    end()
                elif (
                    ("1_pick_1" in pot and "2_pick_3" in pot and "3_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot and "3_pick_3" in pot)
                    or ("1_pick_2" in pot and "2_pick_1" in pot and "3_pick_3" in pot)
                ):
                    pot["5_pick_4"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                    end()
                elif "3_pick_1" in pot and "1_pick_2" in pot:
                    pot["5_pick_3"] = None
                    sprint(
                        "You step on the switch and the grate opens. But the energy beam blocks your path to the ladder.\n"
                    )
                elif (
                    ("2_pick_1" in pot and "3_pick_2" in pot)
                    or ("3_pick_1" in pot and "2_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot)
                    or ("2_pick_1" in pot and "1_pick_2" in pot)
                    or ("1_pick_1" in pot and "3_pick_2" in pot)
                ):
                    pot["5_pick_3"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                elif "2_pick_1" in pot or "4_pick_1" in pot or "1_pick_1" in pot:
                    pot["5_pick_2"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
                else:
                    pot["5_pick_1"] = None
                    sprint(
                        "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
                    )
    else:
        while True:
            level3()
            text = option()
            if text not in ["1", "2", "3", "4", "5"]:
                print("invalid entry")
                continue
            if text not in level_three:
                print("Option no longer accessible")
                continue
            if text == "1":
                del level_three["1"]
                if (
                    ("2_pick_1" in pot and "3_pick_2" in pot and "4_pick_3" in pot)
                    or ("2_pick_1" in pot and "3_pick_3" in pot and "4_pick_2" in pot)
                    or ("2_pick_2" in pot and "3_pick_1" in pot and "4_pick_3" in pot)
                    or ("2_pick_2" in pot and "3_pick_3" in pot and "4_pick_1" in pot)
                    or ("2_pick_3" in pot and "3_pick_1" in pot and "4_pick_2" in pot)
                    or ("2_pick_3" in pot and "3_pick_2" in pot and "4_pick_1" in pot)
                ):
                    pot["1_pick_4"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                    end()

                elif (
                    ("3_pick_1" in pot and "2_pick_2" in pot)
                    or ("3_pick_1" in pot and "4_pick_2" in pot)
                    or ("2_pick_1" in pot and "3_pick_2" in pot)
                    or ("4_pick_1" in pot and "3_pick_2" in pot)
                ):
                    pot["1_pick_3"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                elif ("2_pick_1" in pot and "4_pick_2" in pot) or (
                    "4_pick_1" in pot and "2_pick_2" in pot
                ):
                    pot["1_pick_3"] = None
                    sprint("You forcefully try to pull the lever and it breaks.\n")
                elif "2_pick_1" in pot or "4_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint("You forcefully try to pull the lever and it breaks.\n")
                elif "3_pick_1" in pot:
                    pot["1_pick_2"] = None
                    sprint(
                        "You pull the lever and it releases the ladder and unlatches the mirror frame. But unfortunately it also unlocks the door!\nThe guards are now closing in on your position.\n"
                    )
                else:
                    pot["1_pick_1"] = None
                    sprint("You forcefully try to pull the lever and it breaks.\n")
            elif text == "2":
                del level_three["2"]
                if (
                    ("1_pick_3" in pot and "3_pick_1" in pot and "4_pick_2" in pot)
                    or ("1_pick_3" in pot and "3_pick_2" in pot and "4_pick_1" in pot)
                    or ("1_pick_1" in pot and "3_pick_2" in pot and "4_pick_3" in pot)
                    or ("1_pick_1" in pot and "3_pick_3" in pot and "4_pick_2" in pot)
                    or ("1_pick_2" in pot and "3_pick_3" in pot and "4_pick_1" in pot)
                ):
                    pot["2_pick_4"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                    end()
                elif "1_pick_2" in pot and "3_pick_1" in pot and "4_pick_3" in pot:
                    pot["2_pick_4"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out. The mirror redirects it towards the guards. The guards can no longer move.\n"
                    )
                    end()
                elif (
                    ("1_pick_1" in pot and "3_pick_2" in pot)
                    or ("1_pick_1" in pot and "4_pick_2" in pot)
                    or ("3_pick_1" in pot and "1_pick_2" in pot)
                    or ("4_pick_1" in pot and "1_pick_2" in pot)
                    or ("4_pick_1" in pot and "3_pick_2" in pot)
                    or ("3_pick_1" in pot and "4_pick_2" in pot)
                ):
                    pot["2_pick_3"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                elif "1_pick_1" in pot or "3_pick_1" in pot or "4_pick_1" in pot:
                    pot["2_pick_2"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
                else:
                    pot["2_pick_1"] = None
                    sprint(
                        "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
                    )
            elif text == "3":
                del level_three["3"]
                if (
                    ("1_pick_1" in pot and "2_pick_2" in pot and "4_pick_3" in pot)
                    or ("1_pick_1" in pot and "2_pick_3" in pot and "4_pick_2" in pot)
                    or ("1_pick_2" in pot and "2_pick_1" in pot and "4_pick_3" in pot)
                    or ("1_pick_2" in pot and "2_pick_3" in pot and "4_pick_1" in pot)
                    or ("1_pick_3" in pot and "2_pick_1" in pot and "4_pick_2" in pot)
                    or ("1_pick_3" in pot and "2_pick_2" in pot and "4_pick_1" in pot)
                ):
                    pot["3_pick_4"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                    end()
                elif (
                    ("2_pick_1" in pot and "1_pick_2" in pot)
                    or ("4_pick_1" in pot and "1_pick_2" in pot)
                    or ("1_pick_1" in pot and "4_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot)
                    or ("2_pick_1" in pot and "4_pick_2" in pot)
                    or ("4_pick_1" in pot and "2_pick_2" in pot)
                ):
                    pot["3_pick_3"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                elif "2_pick_1" in pot or "4_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "You apply the lubricant on the lever and it becomes functional.\n"
                    )
                elif "1_pick_1" in pot:
                    pot["3_pick_2"] = None
                    sprint(
                        "You attempt to lubricate the lever but it’s already damaged.\n"
                    )
                else:
                    pot["3_pick_1"] = None
                    sprint(
                        "You apply the lubricant on the lever and it becomes functional"
                    )
            else:
                del level_three["4"]
                if (
                    ("1_pick_3" in pot and "2_pick_1" in pot and "3_pick_2" in pot)
                    or ("1_pick_3" in pot and "2_pick_2" in pot and "3_pick_1" in pot)
                    or ("1_pick_2" in pot and "2_pick_3" in pot and "3_pick_1" in pot)
                ):
                    pot["4_pick_4"] = None
                    sprint(
                        "You try to align the mirror in front of the beam but the beam zaps you when you come close.\n"
                    )
                    end()
                elif (
                    ("1_pick_1" in pot and "2_pick_3" in pot and "3_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot and "3_pick_3" in pot)
                    or ("1_pick_2" in pot and "2_pick_1" in pot and "3_pick_3" in pot)
                ):
                    pot["4_pick_4"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
                    end()
                elif "3_pick_1" in pot and "1_pick_2" in pot:
                    pot["4_pick_3"] = None
                    sprint(
                        "You take the mirror and align it at a specific position right in front of the wall switch.\n"
                    )
                elif (
                    ("2_pick_1" in pot and "3_pick_2" in pot)
                    or ("3_pick_1" in pot and "2_pick_2" in pot)
                    or ("1_pick_1" in pot and "2_pick_2" in pot)
                    or ("2_pick_1" in pot and "1_pick_2" in pot)
                    or ("1_pick_1" in pot and "3_pick_2" in pot)
                ):
                    pot["4_pick_3"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
                elif "2_pick_1" in pot or "3_pick_1" in pot or "1_pick_1" in pot:
                    pot["4_pick_2"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
                else:
                    pot["4_pick_1"] = None
                    sprint(
                        "You forcefully attempt to pull out the mirror but it breaks.\n"
                    )
