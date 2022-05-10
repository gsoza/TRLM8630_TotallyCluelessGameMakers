# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define b = Character("Barista")
define z = Character("[name]")
define c = Character("Cop")
define h = Character("Hobo")
define p = Character("[pet]")
define g = Character("Sad Girl")
define dog = Character("Dog")
define n = Character(None, what_font="Luminari.ttf", what_xalign=0.5, window_xalign=0.5, window_yalign=0.5, what_text_align=0.5)
define v = Character("Vending Machine")
define a = Character("Locker Attendant")
define items = []
define locker =Character("Locker")

image zombie = "zombie.png"
image protagonist = "protagonist.png"
image barista = "barista.png"
image cop = "police.png"
image apartmentExterior = "Apartment_exterior.png"
image park = "park.png"
image hobo = "hobo.png"
image sadGirl = Transform("sad_girl.png", xzoom=-1)
image dog = "Lost-doggie.png"
image flipdog = Transform("Lost-doggie.png", xzoom=-1)
image street = "Street.png"
image vending = Transform("vending.png", xzoom=-1)
image bedroom = "bedroom.png"
image locker = "rick.png"
image station = "trainstation.png"

    # background images
image coffee = "coffee.png"
image outside = "City_Afternoon.png"


init python:
    showitems = False

    def display_items_overlay():
        if showitems:
            inventory_show = "Inventory: "
            for i in range(0, len(items)):
                item_name = items[i].title()
                if i > 0:
                    inventory_show += ", "
                inventory_show += item_name
            ui.frame()
            ui.text(inventory_show)
    config.overlay_functions.append(display_items_overlay)

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

# The game starts here.



label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ name = renpy.input("What is your name?")
    $ name = name.strip() or "Gary"
    $ pet = renpy.input("What is the last thing you ate?")
    $ pet = pet.strip() or "Vitamin D"

    play music "audio/stairs-into-the-unknown-dark-piano-music-1497.mp3"
    n "Two years have passed, since Covid-57 struck the nation."
    n "Families were forced to stay indoors to prevent the virus from spreading."
    n "Finally the lockdown has been lifted. Some were overjoyed at the opportunity to go out into the world again, socialize, see their friends, go to parties, coffee shops, shopping malls."
    n "But others felt the effects of the long-term isolation."
    n "The world was no longer a friendly place, and the very thought of seeing people..."
    n "..."
    n "6 months have passed since the lockdown was lifted."
    n "However, [name] did not dare step outside the front door, but instead remained within the walls of the apartment, only with [pet] as company."
    n "Little did [name] know, all of this was about to change..."

    scene bedroom
    with fade

    n "[name] wakes up as usual, turns on the laptop and finds a message from a strange email address...the message reads: \"We have [pet], do not try and find us...if you ever want to see [pet] again, follow these instructions:"
    n "1. Go to LOCATION and retrieve the briefcase in the locker 420
    \n2. Bring this item with all of its contents to this location ADDRESS
    \n3. Do not delay"
    stop music fadeout 3.0
    $ showitems = True

label middle:
    stop music fadeout 2.0
    stop sound
    scene apartmentExterior
    menu :
         "Check the Park":
             jump park
         "Head down the street":
             jump street
         "Go to the locker":
             jump locker

    #label destination_choice1:
        #jump coffeeShop

    #label destination_choice2:
    #    jump park

    #label destination_choice3:
    #    jump booze

label park:
    scene park

    play music "audio/urban.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show zombie at slightright

    show sadGirl at slightleft

    z "Um...hi"
    g "Can you help me find my doggie? I LOST MY DOGGIE"

    menu:
        "Heck no kiddo, dogs are GROSS":
            jump sadGirlChoice_rude
        "You poor thing, of course I can!":
            jump sadGirlChoice_good
        "I wish I could":
            jump sadGirlChoice_nothing

    label sadGirlChoice_rude:
        g "You big meanie"
        n "That was a pretty jerk move, come back when you learn not to bully little girls."
        jump middle

    label sadGirlChoice_good:
        g "You're so nice!"
        jump searchPark

    label sadGirlChoice_nothing:
        g "*cry* please come back if you can!"
        jump middle

label searchPark:
    scene park
    show zombie at slightright
    "Where should I look?"
    menu search:
        "Behind the tree":
            show dog at slightleft
            play sound "audio/woof.mp3"
            "The dog is here! Let's go find the little girl"
            jump foundDog
        "Behind the bush":
            "All I see is a broken bottle, an empty cigarette pack, and a bloody ear...eww..Let's look somewhere else"
            jump search
        "Under a rock":
            "There's a beetle! But...that's not a dog"
            jump search

label foundDog:
    scene park
    show zombie at slightright
    show flipdog at slightright
    show sadGirl at slightleft
    play sound "audio/panting.mp3"
    g "You found him! Thank you so much! Here, take this."
    "You got {b}loose change: $0.69{/b}"
    $ items.append("change")
    jump middle

label street:
    scene street
    show zombie at slightright
    z "Man, it's so hot today, I could really use a drink right now..."
    z "Oh look, a vending machine, perfect!"
    show vending at left
    v "Spare some change?"

    menu vending:
        "Holy sh*t, a talking vending machine! Stay away from me":
            v "Wow, that was rude."
            n "Vending machines are people too...sorta...anyway be nice."
            jump middle
        "Sure, but this is all I have":
            if "change" not in items:
                "what is this a trick? it's just your hand. Got any {i}actual{/i} change??"
                jump vending
            else:
                $ items.remove("change")
                v "MMMMM, DELICIOUS, LOOSE CHANGE. Here, take this."
                "A {b}key{/b} drops out of the vending machine's {i}mouth{/i}"
                $ items.append("key")
                z "But...what about my drink..."
                v "..."
                z "oh well"
                jump middle
        "I wish I could":
            v "Well I'll be right here if you {i}change{/i} your mind."
            jump middle

label locker:
    scene station
    show zombie at slightright
    show locker at slightleft
    z "Okay, I made it to the locker. Let's get this over with"
    menu openLocker:
        "Insert key":
            if "key" not in items:
                z "Uh, I don't have anything to open this with"
                jump openLocker
            else:
                jump lockerTalk
        "Leave":
            jump middle

label lockerTalk:
    locker "Hey kid, what's the big idea? You trying to stick some random junk in me? Buy me dinner first!"
    z "...Another talking object"
    menu lockerResponse:
        "F*ck this sh*t, I'm out":
            play music "audio/fuck.mp3"
            n "yeah you gangsta, now come back when you wanna play nice"
            jump middle
        "That's cool.":
            locker "meh, another day then."
            jump openLocker
        "Will you let me stick this key in you and get the breifcase?":
            locker "You kiddin' me? Do I look like I got a keyhole? Kids these days, gotta tell 'em how to do everything I tell ya."
            menu:
                "Dude, you're a dick":
                    jump gameOver
                "Ok, what should I do then?":
                    jump explain
                "I don't know what a keyhole looks like":
                    jump explain
            label explain:
                locker "Alright alright, I'll help ya out kid. It's easy. Alls ya gotta do is go up to that guy at the stand over there. He can give ya the combination. Easy right?"
                z "Ok, here goes."
                scene station
                show barista at slightleft
                show zombie at slightright
                a "Hiya! How can I help you?"
                menu attendant:
                    "Will you marry me?":
                        n "It was at that moment...he knew he fucked up"
                        jump gameOver
                    "(stuttering) Can you..h..help me t..t..to open locker 420 p..please?":
                        jump combination
                    "GIMME THE F*CKING LOCKER COMBINATION":
                        n "That was intense"
                        jump gameOver

label combination:
    n "yay you got the thing and everyone dies, how bout some coffee?"
    scene coffee
    play music "audio/coffee.mp3"
    show barista at slightleft
    show zombie at slightright
    b "Hi, welcome to Zombucks, how can I help you?"
    z "Didn't I just see you at...uh...nevermind"
    menu drinkchoice:
        "Need…coffee…*groan*":
            b "Hmm, let’s get you caffeinated."
            z "Caffeine good"
            jump choice_done
        "One bloody chai, please":
            b "Come again? Do you mean dirty chai?"
            z "uh...I guess"
            jump choice_done
        "I’ll have a vanilla oat decaf double shot mocha frappuccino with a twist":
            b "I see this isn’t your first time! One basic-white-girl coming right up!"
            z "Thanks fellow human!"
            jump choice_done


    label choice_done:
        hide barista
    "*barista goes to make drink*"

    z "I swear that was the same person from..."
    show barista at slightleft
    b "Order up!"
    z "*almost falls over*"
    jump gameWin

label gameOver:
    n "You have failed as a human. YOU LOSE"
    return
label gameWin:
    n "You have regained your humanity. YOU WIN"
    return
