import time
import sys
import random

item = ""
equipped_item = "scalpel"
items = ["metal tube", "baseball bat", "broken glass bottle"]
item_damage = 20
enemy_health = 50


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You wake up lying in what that looks like a hospital bed.")
    print_pause("There are wires of different colors connecting you to \n"
                "a vital signs and EEG monitor")
    print_pause("There's a long tube connecting you to a portable IV pole \n"
                "through a needle in your right forearm")
    print_pause("You don't have any recollections of what might have \n"
                "possibly happened to you")
    print_pause("Besides, the hospital looks abondoned with all the stuff \n"
                "scattered all over place.")
    print_pause("You have a very bad feeling about all this")


def room1():
    print_pause("You have this feeling of numbness in the entire left part \n"
                "of your body.")
    print_pause("Despite this you try free yourslef of all that\n"
                "wires and tube,so you can explore the place\n"
                "and find out what happened.")
    room1_response()


def room1_response():
    response = input("Which one you take out first? \n"
                     "1. You try to remove the wires connecting you to the\n"
                     "monitor first.\n"
                     "2. You try to free your right forearm from the needle\n"
                     "connecting you to the portable IV pole. \n")
    if response == "1":
        print_pause("You decide not to unplug your forearm from the\n"
                    "IV pole. After all you don't feel very well and\n"
                    "though your forearm is sore, it seems it's better\n"
                    "to keep it connected to that IV bag and walk \n"
                    "with that pole in your right hand instead.")
        print_pause("You look around the room and take a scalpel in your \n"
                    "left hand before going out.")
        corridor(equipped_item, item_damage)
    elif response == "2":
        print_pause("You feel the pain caused by the needle in your \n"
                    "right forearm suddenly goes away.")
        print_pause("But before you have a chance to have a sigh of relief \n"
                    "your heart beat increases wildly and you feel you're\n"
                    "about to faint any moment.")
        print_pause("You fall to the ground and die instantly without even \n"
                    "having the chance to think about what was in\n"
                    "that IV bag.")
        game_over()
    else:
        room1_response()


def corridor(equipped_item, item_damage):
    print_pause("You're now in a long corridor with creepy flickering \n"
                "lights")
    print_pause("You can go directly to the reception counter at\n"
                "the end of the coridor or you can check the room\n"
                "next to your room where you can hear a strange\n"
                "moaning sound is coming from")
    corridor_response(equipped_item, item_damage)


def corridor_response(equipped_item, item_damage):
    response = input("What whould you do? \n"
                     "1. Go to the reception counter \n"
                     "2. Go check the other room \n"
                     "3. Go back to your room \n")
    if response == "1":
        if equipped_item != "scalpel":
            print_pause("There is nothing else to do here. You head back \n"
                        "to the corridor.")
            corridor(equipped_item, item_damage)
        else:
            reception_counter(equipped_item, item_damage)
    elif response == "2":
        room2(equipped_item, item_damage)
    elif response == "3":
        print_pause("You've already done all the things in your room. \n"
                    "It's time to venture out and find out what\n"
                    "happened to you. You go back to the corridor again")
        corridor(equipped_item, item_damage)
    else:
        corridor_response(equipped_item, item_damage)


def reception_counter(equipped_item, item_damage):
    item = random.choice(items)
    print_pause("You look behind the reception counter. There are lots of \n"
                "scattered papers and folders.\n"
                "There is a " + item + " leaning on the \n"
                "back wall. You can see fresh blood dripping the sides \n"
                "of the " + item + " as if it has been used recently.")
    reception_response(item, item_damage)


def reception_response(item, item_damage):
    global equipped_item
    response = input("What would you do? \n"
                     "1. Put down the scalpel and grab\n"
                     "the " + item + " instead, then\n "
                     "head back to the corridor \n"
                     "2. Take nothing and just go back to the corridor \n")
    if response == "1":
        item_damage = random.randint(40, 100)
        equipped_item = item
        corridor(equipped_item, item_damage)
    elif response == "2":
        corridor(equipped_item, item_damage)
    else:
        reception_response(equipped_item, item_damage)


def room2(equipped_item, item_damage):
    print_pause("You gently push the door away to see the back of\n"
                "a shadow-like figure sitting on a bed. You can\n"
                "hear him whispering something to \n"
                "himself but it's like muttering nonesense.")
    print_pause("You press your " + equipped_item + " in hand \n"
                "as you try to approach him from behind unnoticed.\n"
                "As you take your first step \n"
                "the screeching sound of the IV pole makes him aware.")
    print_pause("He just turns back towards you and for a moment you freeze \n"
                "on the spot to see his hands and mouth soaked red in blood.")
    print_pause("Before you can even scream he jumps at you. \n"
                "Now it's only you and your " + equipped_item + " against\n"
                "this frenzied beast of a man")
    room2_response(equipped_item, item_damage)


def room2_response(equipped_item, item_damage):
    response = input("What would you do? \n"
                     "1. Attack him \n"
                     "2. Run back to the corridor and lock the door \n")
    if response == "1":
        if item_damage < enemy_health/2:
            print_pause("Your " + equipped_item + " was certainly\n"
                        "not enough to stop him.")
            print_pause("Alas, it's too late to do anything about it.")
            print_pause("Last thing you remember was a excruciating pain")
            game_over()
        elif item_damage > enemy_health/2 and item_damage < enemy_health:
            print_pause("You involuntarily slash\n"
                        "your " + equipped_item + " up and down \n"
                        "his chest.")
            ending1()
        elif item_damage > enemy_health:
            print_pause("You close your eyes and use all the strength\n"
                        "in your left hand moving\n"
                        "the " + equipped_item + " right\n"
                        "and left with maximum force.")
            ending2()
    elif response == "2":
        corridor(equipped_item, item_damage)
    else:
        room2_response(equipped_item, item_damage)


def ending1():
    print_pause("You feel a constant splash of blood on your\n"
                "face and while you got him, there is this immense pain\n"
                "and a sharp burning sense in your left thigh.")
    print_pause("All of a sudden, he falls like a rag doll\n"
                "soaked in blood and you can hear a hissing\n"
                "sound that stops after a short while.")
    print_pause("He's dead but you're in a really bad shape too. Blood is \n"
                "coming out of your left thigh non-stop and you\n"
                "know if you fail to stop this somehow, it will\n"
                "only be a matter of minutes until you end up \n"
                "like him.")
    win()


def ending2():
    print_pause("You can hear a thumping sound followig screams of pain.")
    print_pause("You open your eyes to see his overwhelmingly bludgeoned\n"
                "body lying motion-less on the ground.")
    print_pause("You can't believe that you killed him with not\n"
                "a single scratch on your body.")
    win()


def win():
    print_pause("Congratulations on finishing part one of the story.")
    print_pause("Please stay tuned for the relaese of the second part.")
    print_pause("To be continued ...")
    sys.exit()


def game_over():
    print_pause("Game Over")
    response = input("Do you want to play again? \n"
                     "Press Y or N for Yes or No\n").lower()
    if response == "y":
        intro()
        room1()
    elif response == "n":
        print_pause("Thank you for playing! See you next time.")
        sys.exit()
    else:
        game_over()


def play_game():
    intro()
    room1()
    corridor()
    reception_counter()
    room2()


play_game()
