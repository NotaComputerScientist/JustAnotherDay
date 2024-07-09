# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]")

define cornelius = Character("Cornelius")
define elyaha = Character("Elyaha")
define chuck = Character("Chuck")
define sorasan = Character("Sora-San")
define freddy = Character("Freddy")
define liza = Character("Liza")

image iCornelius = "cornelius.png"
image iElyaha = "elyaha.png"
image iChuck = "chuck.png"
image iSorasan = "sorasan.png"
image iFreddy = "freddy.png"
image iLiza = "liza.png"
# The game starts here.

label start:

    default preferences.text_cps = 48

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    python:
        one = Position(xpos=0)
        two = Position(xpos=0.2)
        three = Position(xpos=0.4)
        four = Position(xpos=0.6)
        five = Position(xpos=0.8)
        six = Position(xpos=0.9)

    scene 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "This story takes place months after the end of the world. After hearing a mysterious radio signal,  you and a group of refugees managed to find an abandoned bunker for the super rich."

    "The world outside the bunker was horrible. Death, abominations, radioactive waste, and Lovecraftian magic plagued every square inch of what remained. But here you are safe."

    "However, hiding in a bunker after the end of the world had one unexpected consequence: boredom. No more new shows, Taylor Swift albums, walks in the park, or short form videos to occupy your limited time on Earth."

    "Naturally, this has left the survivors in your bunker, who are all 20 something and single, anxious for a date."

    "Fortunately, there is a plot convenient terraforming machine in your bunker that is set to go off in a week and bring some life back to the wasteland. This device would see the gray, scorched Earth turn back to the vibrant greens and browns of trees and plants."

    "Everyone wants to find a date for this spectacular event, hopefully with someone whom they can start a life with in this new, strange world."

    python:
        povname = renpy.input("Before we continue, what's your name?", length=32)
        povname = povname.strip()

        if povname == "":
            povname = "He/She/They who shall not be named"

    "Nice to meet you, [povname]."

    "Now, let me introduce you to your potential love interests."

    show iCornelius
    "Meet Cornelius, a cyborg veteran of the Great War."
    "Some say he lost his soul fighting the abominations, others say it was when he augmented himself with steel."
    "Regardless, there’s still a beating heart under his dark, grizzled exterior."
    hide iCornelius

    show iElyaha
    "Meet Elyaha, Queen Elyaha to be specific."
    "She was trained from a young age by a group of the best educators to take the throne from her father. When the war came she lost her kingdom, potential throne, and people."
    "Embittered and alone, she tries to find meaning in this post apocalypse."
    hide iElyaha

    show iChuck
    "Meet Chuck, former college athlete and amateur nutritionist."
    "When the war came he fought through the abominations, enemy soldiers, and radiation to bring his little sister to safety."
    "After making it to the bunker, Chuck felt restless instead of relief."
    hide iChuck

    show iSorasan
    "Meet Sora-San, a catgirl with a scar across her face."
    "People describe her as either flirty or off putting, either way nobody seems to know much about her."
    hide iSorasan

    show iFreddy
    "Meet Freddy, a socially awkward techno wizard with golden retriever energy."
    "He came here after discovering the leadership of his academy experimented on some of the survivors."
    "He hopes to find a family in this new community, and hopefully a partner."
    hide iFreddy

    show iLiza
    "And finally, meet Liza, a math and computer nerd who always seems to be reading a book."
    "She always answers questions with sarcasm or a quip."
    hide iLiza

    "Now that you've met the whole gang, which one of these eligible bachelor(ette)s tickles your fancy?"

    label lovechoice:

    show iCornelius at one
    show iElyaha at two
    show iChuck at three
    show iSorasan at four
    show iFreddy at five
    show iLiza at six
    menu:
        "Choose Cornelius":
            define love = cornelius
        "Choose Elyaha":
            define love = elyaha
        "Choose Chuck":
            define love = chuck
        "Choose Sora-San":
            define love = sorasan
        "Choose Freddy":
            define love = freddy
        "Choose Liza":
            define love = liza

    "Are you sure you want to choose [love]?"
    menu:
        "Yes.":
            "Great!"
        "Choose someone else.":
            jump lovechoice
        




    # This ends the game.

    return
