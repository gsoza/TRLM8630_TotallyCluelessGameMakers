# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define b = Character("Barista")
define z = Character("[name]", image="protagonist")
define c = Character("Cop")
define h = Character("Hobo")
define p = Character("[pet]")
define g = Character("Sad Girl")
define dog = Character("Dog")
define n = Character(None, what_font="Luminari.ttf", what_xalign=0.5, window_xalign=0.5, window_yalign=0.5, what_text_align=0.5, what_size = 35)
define v = Character("Vending Machine")
define a = Character("Locker Attendant")
define items = []
define locker =Character("Locker")
define park_level = False
define street_level = False
define locker_level = False
define protag = ""

image protagonist = Transform("[protag].png", xzoom=-1)
image protagonist happy = Transform("[protag]_happy.png", xzoom=-1)
image barista = "barista.png"
image cop = "police.png"
image apartmentExterior = "Apartment_exterior.png"
image park = "park.png"
image hobo = Transform("hobo.png", xzoom=-1)
image girl sad = "girl_sad.png"
image girl happy = "girl_happy.png"
image girl mad = "girl_mad.png"
image dog sad= "dog_sad.png"
image dog happy= "dog_happy.png"
image dog mad= "dog_mad.png"
image flipdog happy = Transform("dog_happy.png", xzoom=-1)
image street = "Street.png"
image vending = Transform("vending.png", xzoom=-1)
image bedroom = "bedroom.png"
image locker = "rick.png"
image station = "trainstation.png"
image alley = "alley.png"
image bg black = "#000000"
image bg party = "party.jpeg"
image pet = "iguana.png"
image Protag1 = "Protagonist1.png"
image Protag2 = "Protagonist2.png"

    # background images
image coffee = "coffee.png"
image outside = "City_Afternoon.png"

# screen choose:
#       imagebutton:
#           auto "Protagonist1_%s.png"
#           xalign 0.2
#           yalign 0.6
#           action Jump("choose_male")
#       imagebutton:
#           auto "Protagonist2_%s.png"
#           xalign 0.8
#           yalign 0.6
#           action Jump("choose_female")

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

init python:
    credits = ('Programming', 'Christopher Dean'), ('Narrative Design', 'Xinxin Huang'), ('Narrative Design', 'Gary Soza'),('Project Management', 'Baoze Zhang'), ('Character Illustration', 'Marianna Gutierrez'), ('Intro Music: "Delayed Response"', 'Kei Lam'), ('Localization: Spanish', 'Christopher Dean'), ('Localization: Spanish', 'Gary Soza'), ('Localization: Spanish', 'Marianna Gutierrez'), ('Localization: Simplified Chinese', 'Xinxin Huang'),('Localization: Simplified Chinese', 'Baoze Zhang')
    credits_s = "{size=60}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.15.7.374" #Don't forget to set this to your Ren'py version

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)

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
    $ name = renpy.input(_("What is your name?"))
    $ name = name.strip() or "Gary"
    $ pet = renpy.input(_("What is the last thing you ate?"))
    $ pet = pet.strip() or "Vitamin D"

    # show screen choose
    # label chose_male:
    #     $protagonist = "Protagonist1.png"
    # label chose_female:
    #     $protagonist = "Protagonist2.png"


label story:



    play music "audio/stairs-into-the-unknown-dark-piano-music-1497.mp3"
    n "Two years have passed, since Covid-57 struck the nation."
    n "Families were forced to stay indoors to prevent the virus from spreading."
    n "Finally the lockdown has been lifted. Some were overjoyed at the opportunity to go out into the world again, socialize, see their friends, go to parties, coffee shops, shopping malls."
    n "But others felt the effects of the long-term isolation."
    n "The world was no longer a friendly place, and the very thought of seeing people..."
    n "..."
    n "6 months have passed since the lockdown was lifted."
    n "However, you, [name] did not dare step outside your front door, but instead remained within the walls of your apartment, only with your pet Iguana, [pet] as company."
    n "Little did [name] know, all of this was about to change..."

    scene bedroom
    with fade

    n """[name] wakes up as usual, turns on the laptop and finds a message from a strange email address...the message reads:

    \"We have [pet], do not try and find us...if you ever want to see [pet] again, follow these instructions:\"

    *The note instructs you to complete a series of tasks that will lead you to a briefcase in locker #420 located at the train station.

    From there you will take said briefcase to a specified location.*"""

    stop music fadeout 3.0
    $ showitems = True

label characterChoice:
    show Protag1 at left
    show Protag2 at right
    menu:
        # "{image=Protagonist1.png}":
        "<- Character 1":
            $ protag = "Protagonist1"
            hide Protag1
            hide Protag2
            jump middle
        # "{image=Protagonist2.png}":
        "Character 2 ->":
            $ protag = "Protagonist2"
            hide Protag1
            hide Protag2
            jump middle
label middle:
    stop music fadeout 2.0
    stop sound
    scene apartmentExterior
    show protagonist at slightright
    menu decision:
         "Check the Park":
             if park_level:
                 "I don't think I need to go there again"
                 jump decision
             else:
                 jump park
         "Head down the street":
             if street_level:
                "I don't think I need to go there again"
                jump decision
             else:
                jump street
         "Go to the locker":
             if locker_level:
                "I don't think I need to go there again"
                jump decision
             else:
                jump locker
         "Go to the location":
             if "briefcase" in items:
                jump location
             else:
                "Better not show up empty-handed"
                jump decision

label park:
    scene park

    play music "audio/urban.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show protagonist at slightright

    show girl sad at slightleft

    z "Um...hi"
    g "Can you help me find my doggie? I LOST MY DOGGIE"

    menu:
        "Heck no kiddo, dogs are GROSS":
            jump sadGirlChoice_rude
        "Uh, sure...I can look around":
            jump sadGirlChoice_good
        "I wish I could":
            jump sadGirlChoice_nothing

    label sadGirlChoice_rude:
        show girl mad at slightleft
        g "You big meanie"
        n "That was a pretty jerk move, come back when you learn not to bully little girls."
        jump middle

    label sadGirlChoice_good:
        show girl happy at slightleft
        g "You're so nice!"
        jump searchPark

    label sadGirlChoice_nothing:
        g "*cry* please come back if you can!"
        jump middle

label searchPark:
    scene park
    show protagonist at slightright
    "Where should I look?"
    menu search:
        "Behind the tree":
            show dog sad at slightleft
            play sound "audio/woof.mp3"
            z @ happy "Hey I found it! Come on boy!"
            show dog mad at slightleft
            z "Hmm, he doesn't want to come with me"
            if "toy" in items:
                menu:
                    "Give toy":
                        $ items.remove("toy")
                        show dog happy
                        z @ happy "Let's go find your mom!"
                        jump foundDog
            else:
                "Maybe I should find something to give him"
                hide dog mad
                jump search
        "Behind the bush":
            "All I see is a broken bottle, an empty cigarette pack, and a bloody ear...eww..Let's look somewhere else"
            jump search
        "Under a rock":
            "I found a beetle...wait, I see a chew toy as well!"
            menu:
                "Take toy":
                    $ items.append("toy")
                    "Hmm, I bet he'll like this!"
                    jump search
                "Leave toy":
                    jump search

label foundDog:
    scene park
    show protagonist at slightright
    show flipdog happy at slightright
    show girl happy at slightleft
    play sound "audio/panting.mp3"
    g "You found him! Thank you so much! Here, take this."
    "You got {b}loose change: $0.69{/b}"
    $ items.append("change")
    $ park_level = True
    jump middle

label street:
    scene street
    show protagonist at slightright
    z "Man, it's so hot today, I could really use a drink right now..."
    z "Oh look, a vending machine, perfect!"
    show vending at left
    v "Spare some change?"

    menu vending:
        "What?? A talking vending machine! Stay away from me!":
            v "Wow, that was rude."
            n "Vending machines are people too...sorta...anyway be nice."
            jump middle
        "Sure, but this is all I have":
            if "change" not in items:
                "what is this a trick? It's just your hand. Got any {i}actual{/i} change??"
                jump vending
            else:
                $ items.remove("change")
                v "MMMMM, DELICIOUS, LOOSE CHANGE. Here, take this."
                "A {b}key{/b} drops out of the vending machine's {i}mouth{/i}"
                $ items.append("key")
                z "But...what about my drink?"
                v "..."
                z "oh well"
                $ street_level = True
                jump middle
        "I wish I could":
            v "Well I'll be right here if you {i}change{/i} your mind."
            jump middle

label locker:
    scene station
    show protagonist at slightright
    show locker at slightleft
    z "Okay, I made it to the locker. Let's get this thing open"
    menu openLocker:
        "Open Locker":
            if "key" not in items:
                z "Uh, I don't have anything to open this with."
                jump openLocker
            else:
                "You insert the {b}key{/b}"
                jump lockerTalk
        "Leave":
            jump middle

label lockerTalk:
    locker "Hey kid, what's the big idea? Watch where you're sticking that thing!"
    z "Oh great...another talking object"
    menu lockerResponse:
        "F*ck this sh*t, I'm out":
            play music "audio/fuck.mp3"
            n "yeah you gangsta, now come back when you wanna play nice"
            jump middle
        "I don't have time for this.":
            locker "meh, another day then."
            jump openLocker
        "Look, I'm just trying to get the briefcase inside so I can rescue [pet]":
            locker "Well, I don't know what a [pet] is, but that key ain't gonna work. Kids these days, gotta tell 'em how to do everything I tell ya."
            menu lockerResponse2:
                "Jerk...":
                    n "Again with the social faux-pas"
                    jump lockerResponse2
                "Ok, what should I do then?":
                    jump explain
            label explain:
                locker "You look like a nice kid, I'll help ya out."
                locker "Alls ya gotta do is go up to that guy at the stand over there. He can give ya the combination. Easy right?"
                z "Ok, here goes."
                scene station
                show barista at slightleft
                show protagonist at slightright
                a "Hiya! How can I help you?"
                menu attendant:
                    "*babbles incoherently*":
                        n "The attendant looks at you, confused, then turns away."
                        n "Maybe try using people words"
                        jump attendant
                    "(stuttering) Can you..h..help me t..t..to open locker 420 p..please?":
                        n "The nice attendant helps you to open the locker and appreciates your normal amount of politeness"
                        $ items.remove("key")
                        "You retrieved the {b}briefcase{/b}"
                        $ items.append("briefcase")
                        $ locker_level = True
                        jump middle
                    "GIMME THE LOCKER COMBINATION!":
                        n "That was intense"
                        jump middle
label location:
    scene alley
    show protagonist at slightright
    z "Ok, here we are..."
    "Congratulations, [name]! You made it to the final destination. Hope [pet] is still breathing..."
    z "Who said that??"
    z "I should probably open this door..."
    menu door:
        "Open door":
            jump surprise
        "Run away":
            n "You've come so far, just one more step."
            jump door
label surprise:
    scene bg black
    "SURPRISE!!!"
    z "[pet]??"
    $ items.remove("briefcase")
    scene bg party
    show protagonist at right
    show pet:
        xalign 0.75
        yalign 0.30
    show girl happy at left
    show hobo:
        xalign 0.35
        yalign 1.0
    show dog happy at slightleft
    z "What is all this?"
    h "We arranged this suprise party challenge for you."
    h "We were deeply concerned about you being all alone all the time and wanted you to get out and live again."
    z "It was definitely a strange adventure, but was a lot of fun. I'm glad [pet] is okay!"
    p "*happy noises*"
    jump win


label win:
    n "yay you got the thing and everyone dies, how bout some coffee?"
    scene coffee
    play music "audio/coffee.mp3"
    show barista at slightleft
    show protagonist at slightright
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
    call credits
    return

label credits:
    $ _skipping= False
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return
