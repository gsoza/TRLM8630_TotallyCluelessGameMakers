# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define b = Character("Barista")
define z = Character("Zombie")
define c = Character("Cop")
define h = Character("Hobo")

image zombie = "zombie.png"
image barista = "barista.png"
image cop = "police.png"
image apartmentExterior = "Apartment_exterior.png"
image park = "park.png"
image hobo = "hobo.png"

    # background images
image coffee = "coffee.png"
image outside = "City_Afternoon.png"




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

    scene apartmentExterior
    with fade

    show zombie at slightright

    z "Finally, I'm outside, enjoying the sun"
    z "Where should I go next?"


    label destination1:
        $caffeinated = False
    menu :
         "Coffee Shop":
             if caffeinated:
                 "I think I've had enough lattes for one day"
                 jump destination1
             else:
                 "need bean juice make energy"
                 jump destination_choice1
         "Park":
            if caffeinated:
                jump destination_choice2
            else:
                "*groan*...no energy...can't make it"
                jump destination1
         "Bar":
             if caffeinated:
                 jump destination_choice3
             else:
                "*groan*...no energy...can't make it"
                jump destination1

    label destination_choice1:
        jump coffeeShop

    label destination_choice2:
        jump park

    label destination_choice3:
        jump booze

label coffeeShop:
    scene coffee

    play music "audio/coffee.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show zombie:
        xalign 0.75
        yalign 1.0

    z "Humans like coffee, I should be able to find someone here..."

    show barista:
        xalign 0.25
        yalign 1.0


    # These display lines of dialogue.

    b "Hi there! Welcome to “Fake starbucks name”, how can I help you?"
    z "Oh, where'd you come from? Uh..."
    menu:
        "Need…coffee…*groan*":
            jump choice1_semi
        "One bloody chai, please":
            jump choice1_zombie
        "I'll have a vanilla oat decaf quadruple shot mocha frappuccino.":
            jump choice1_human

    label choice1_semi:
        b "Hmm, let’s get you caffeinated."
        z "Caffeine good"
        jump choice1_done


    label choice1_zombie:
        b "Come again? Do you mean dirty chai?"
        z "uh...I guess"
        jump choice1_done

    label choice1_human:
        b "I see this isn’t your first time! One basic-white-girl coming right up!"
        z "Thanks fellow human!"
        jump choice1_done


    label choice1_done:
        hide barista
    "*barista goes to make drink*"

    z "That was a close one..."
    show barista at slightleft
    b "Order up!"
    z "uh...*groan*"
    $ caffeinated = True
    jump destination2
label destination2:
    menu:
        "Park":
            jump destination_choice2
label park:
    scene park
    with fade


    play music "audio/urban.wav"

    show zombie at slightright
    z "Ok now what?"
    z "Maybe I'll just stand here and wait for a human..."

    show hobo at slightleft with move

    h "LDKJFOPIELKFJDFlkjls;dfjweo"
    z "Uh oh"
    # This ends the game.

    return
