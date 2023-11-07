from pyfiglet import Figlet
import config
from permutations import first, second, third, sprint, level, level2, level3

level_one = config.level_one
level_two = config.level_two
level_three = config.level_three

fig = Figlet()
pick_font = fig.getFonts()
fig.setFont(font="standard")


def main():
    sprint(
        "In the darkness of night, a group of witches stole into your village taking with them the orb of ancient wonders, an artifact sacred to your community. \nYou accidently witnessed the whole thing and so the witches have taken you hostage to their castle high upon the mountains.\nIt is up to you to devise a means of retrieving the treasure and escaping back to your village."
    )
    input("Press Enter to continue")
    sprint(
        "The witches aren’t so smart so the game is fairly simple. For each level you’ll be given a list of items to aid your mission.\nYou must use these items in the correct order to succeed. All items can only be used once! \nGoodluck"
    )
    input("Press Enter to continue")
    first_level()
    input("Press Enter to continue")
    second_level()
    input("Press Enter to continue")
    third_level()
    input("Press Enter to continue")
    print(fig.renderText("Epilogue"))
    sprint(
        "Congrats brave civilian. You managed to escape the witches' tower with the orb of ancient wonders clutched safely in your arms.\nNow another adventure awaits you. You're still far from home and high up in the mountains with the witches still close by and in pursuit.\nBut that's a story for another day. \nThanks for playing."
    )


def first_level():
    print(fig.renderText("Level one"))
    sprint("PRISON\n")
    sprint(
        "You’re in a makeshift prison. The door is equipped with a locked wooden bar. Plot your escape\n"
    )
    global level_one
    while True:
        level_one
        level()
        entry = input("Select option: ")

        if entry == "1":
            sprint("You spray the wooden bar with the smelly liquid.\n")
            del level_one["1"]
            first()
            break
        elif entry == "2":
            sprint("You try to set the wooden bar on fire but it doesn’t catch.\n")
            del level_one["2"]
            first()

            break
        elif entry == "3":
            sprint(
                "With a mighty swing, you hit the wooden bar... and your axe breaks. Bummer\n"
            )
            del level_one["3"]
            first()

            break
        elif entry not in ["1", "2", "3"]:
            sprint("invalid entry")
            continue


def second_level():
    print(fig.renderText("Level two"))
    sprint("STORAGE ROOM\n")
    sprint(
        "You slowly make your way towards the storage room carefully avoiding the patrolling guards.\nThe door to the storage room is powered by magic sliding open to guards that possess an enchanted tag. All guards and their dogs possess this tag.\nA guard steps out of the storage room and you hastily dash inside before it magically slides shut. You sight the orb of ancient wonders \nbut it’s been placed on a lowered pedestal that might raise an alarm should you lift it. And if you somehow manage to retrieve the orb, you have \nno idea how to exit the storage room. Luckily there are magical items around that might provide a solution.\n"
    )
    global level_two
    while True:
        level_two
        level2()
        entry = input("Select option: ")

        if entry == "1":
            sprint(
                "You activate the decoy and are marveled by its effects which don’t last long.\n"
            )
            del level_two["1"]
            second()
            break
        elif entry == "2":
            sprint(
                "You put on the mask… And now you look like one of the guards. The effects don’t last long.\n"
            )
            del level_two["2"]
            second()
            break
        elif entry == "3":
            sprint(
                "The goo holds the pedestal in place and you retrieve the orb. But this still triggers a small alarm that attracts the attention of a guard dog.\nIt enters the storage room and glares at you!\n"
            )
            del level_two["3"]
            second()
            break
        elif entry == "4":
            sprint(
                "You inspect the bone wondering what the witches would need an enchanted bone for.\n"
            )
            del level_two["4"]
            second()
            break
        elif entry not in ["1", "2", "3", "4"]:
            print("invalid entry")
            continue


def third_level():
    print(fig.renderText("Level three"))
    sprint("ESCAPE\n")
    sprint(
        "You dash towards the exit, the guards hot in pursuit. Alas the exit has been blocked! You run into the closest room and the door automatically locks.\nIt’s an empty hall devoid of windows. But you spot a closed grate on the roof! All guards are now on alert and have locked in on your position.\nLuckily you spot some peculiar items stationed around... and a plan forms.\n"
    )
    global level_three
    while True:
        level_three
        level3()
        entry = input("Select option: ")

        if entry == "1":
            sprint("You forcefully try to pull the lever and it breaks.\n")
            del level_three["1"]
            third()
            break
        elif entry == "2":
            sprint(
                "You hit the switch and the energy beam shoots out.. hitting the wall at the far corner.\n"
            )
            del level_three["2"]
            third()
            break
        elif entry == "3":
            sprint("You apply the lubricant on the lever and it becomes functional.\n")
            del level_three["3"]
            third()
            break
        elif entry == "4":
            sprint("You forcefully try to remove the mirror and it breaks.\n")
            del level_three["4"]
            third()
            break
        elif entry == "5":
            sprint(
                "You step on the switch and the grate opens. It stays open for a minute and shuts.\n"
            )
            del level_three["5"]
            third()
            break
        elif entry not in ["1", "2", "3", "4", "5"]:
            print("invalid entry")
            continue


if __name__ == "__main__":
    main()
