# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define slowdissolve = Dissolve(1.0)

 
define l = Character("Leo", color = "#75bd79")
define o = Character("Owen", color = "#6751a2")
define n = Character("Nadia", color = "#ff00d9")

transform slightright:
    xalign 0.85
    yalign 0.4

transform slightleft:
    xalign 0.15
    yalign 0.4

transform right:
    xalign 1.0
    yalign 0.4

transform left:
    xalign 0.0
    yalign 0.4

transform center:
    xalign 0.5
    yalign 0.4

# The game starts here.

label start:
    play music "sadaudio.mp3" fadeout 1
 
    scene happyschody
    with slowdissolve
    show excitedowen at slightright
    o "Look! Such an amazing house, although these stairs look really old."
    hide excitedowen
    show talkingleon at slightleft
    l "Be careful, I wouldn't want you to get hurt or something. You know I don't have anyone else left."
    hide talkingleon
    show happyowen at slightright
    o "You gotta be joking! Nothing could possibly happen to me-"
    scene owendead
    show scaredleonleft at right
    l "OH MY GOD- OWEN!-"
    hide scaredleonleft
    show callingleon at right
    l "OWEN STAY WITH ME! I'm calling the ambulance, try to stay with me."

    scene szpital
    with slowdissolve

    show doctor at right
    show leonzalamka at left
    "Doctor" "Unfortunately we did everything in our power to help. We weren't able to save him, he passed at 6:47 PM."
    l "(Owen... you were everything I had, the one and only thing keeping me alive. My life doesn't have a meaning now.)"
    "Doctor" "I'm really sorry for your loss. Come to the hospital office to fill out the forms."

    scene messyyroom
    with slowdissolve
    show leondepressed at center
    l " I haven't seen the sunlight in almost a week, I haven't left my room in such a long time after his death. He was my only family."
    menu:
        l "What can I do?"
        "Go shopping":
            jump choice1_shop
        "Stay at home":
            jump choice1_home

    label choice1_shop:
        l "I'll go shopping, I guess. I'm just rotting in my room anyway."
        $ renpy.movie_cutscene("goshopping.webm")
        l "I'm a little bit more happy."
        
        jump choice1_done

    label choice1_home:
        l "I'm gonna stay in my room."
        l "The outside is scary."
        jump choice1_done

label choice1_done:
    l "I'm out of energy."
    menu:
        l "I need to eat something"
        "Order food with delivery":
            jump choice4_order
        "Go to a cafe":
            jump choice4_cafe
        "Go to grocery store and cook dinner":
            jump choice4_cook
    label choice4_order:
        l "I'll order some food"
        hide leondepressed
        show phoneleon1 at center
        l "*calling*"
        l "Hello, one salami pizza please"
        l "Thanks, bye"
        l "Ugh, it was so hard"
        jump choice4_done
    label choice4_cafe:
        l "I'll go to a cafe"
        scene restaurant
        with slowdissolve
        show leondepressed at center
        l "Yum"
        scene messyyroom
        with slowdissolve
        show leondepressed at center
        l "Cafe was a good idea"
        jump choice4_done
    label choice4_cook:
        l "I'll cook dinner myself"
        scene shop
        with slowdissolve
        show leondepressed at center
        l "Why is everything so expensive?"
        l "I'm going to the register"
        scene messyyroom
        with slowdissolve
        show leondepressed at left
        l "I don't realy like cooking..."
        l "Wow, my food is realy good"
        jump choice4_done

label choice4_done:
    stop music fadeout 1
    scene door
    with slowdissolve
    show talkinggirl at slightleft
    play sound "knock.mp3"
    "Knock knock"
    scene insidedoor
    with slowdissolve
    play music "nadia.mp3" fadeout 2
    show happygirlleft at slightright
    show leondepressed at left
    n "Hey!"
    hide leondepressed
    show leongada1 at left
    l "Hello? Do I know you?"
    l "Who are you?"
    hide happygirlleft
    show nadiagada2 at slightright
    n "Ohh, we went to school and we had some classes together. Remember?"
    hide leongada1
    hide nadiagada2
    show nadiagada1 at center
    stop music fadeout 2
    menu:
        n "Wanna hang out?"
        "Yeah":
            jump choice2_yes
        "Nah":
            jump choice2_no
        "Why would I?":
            jump choice2_maybe
    
    label choice2_maybe:
        hide nadiagada1
        show nadiagada2 at center
        menu:
            n "Cause you're home alone. So do you wanna go?"
            "Yup":
                jump choice2_yes
            "I'll stay home":
                jump choice2_no

    label choice2_yes:
        n "Let's go to the beach."
        l "Ok, cool. Let me change clothes."
        scene beach
        with slowdissolve
        play music "beach.mp3" fadeout 3
        show beachnad1 at right
        show beachleo1 at slightleft
        l "It's so hot and cozy here"
        n "Yeah cool. Wanna swim?"
        hide beachnad1
        hide beachleo1
        show beachnad3 at right
        show beachleo3 at slightleft
        l "No, let's just sit and chill, ok?"
        n "Of course"
        "Some time later"
        n "Gotta go, my number 123 456 789, call anytime."
        hide beachnad3
        hide beachleo3
        show beachnad2 at right
        show beachleo4 at slightleft
        l "Oh, bye."
        stop music fadeout 3
        n "Goodbye honey!"
        hide beachnad2
        hide beachleo4
        show beachleo2 at slightleft
        l "WTF"
        jump choice2_done

    label choice2_no:
        hide nadiagada1
        show nadiacry at center
        n "But I want to spend time with you:( Maybe I can stay at your house?"
        l "OK"
        scene messyyroom
        with slowdissolve
        show shockednadia at slightright
        show leondepressed at left
        n "Wow, what a mess!"
        hide shockednadia
        show cleanwnadia at slightright
        n "Let's clean here"
        hide cleanwnadia
        hide leondepressed
        "Some time later"
        show happygirlleft at slightright
        show leondepressed at left
        n "I need to go now, here's my phone number 123 456 789, call me anytime."
        hide leondepressed
        show leongada1 at left
        l "Ok, bye"
        n "Bye honey"
        hide happygirlleft
        hide leongada1
        show confusedleon at left
        l "(WTF)"
        jump choice2_done

label choice2_done:
    scene messyyroom
    with slowdissolve
    play music "nadiaxleon.mp3" fadeout 4
    show leonhappy1 at left
    l "Oh my- I don't remember that Nadia was so beautiful."
    l "I think I have feelings for her"
    hide leonhappy1
    show phoneleon1 at left
    menu:
        l "Maybe I should text her?"
        "Yes, text her and ask her out.":
            jump choice3_text
        "Yes, she's probably lazy and not doing anything rn.":
            jump choice3_textbad
label choice3_text:
    l "Yes, I'm gonna text her"
    hide phoneleon1
    show phoneleon2 at left
    "Leo: Hi Nadia. What are you doing next weekend?"
    "Ding"
    hide phoneleon2
    show phoneleon3 at left
    l "OMG It's her!"
    hide phoneleon3
    show phoneleon2 at left
    "Nadia: Nothing."
    hide phoneleon2
    show phoneleon1 at left
    "Leo: Do you want to go for dinner?"
    hide phoneleon1
    show phoneleon3 at left
    "Nadia: Yes, please"
    hide phoneleon3
    show phoneleon2 at left
    "Leo: Sunday 7pm?"
    hide phoneleon2
    show phoneleon1 at left
    "Nadia: I'll be there."
    stop music fadeout 3

    scene black
    with slowdissolve
    $ renpy.movie_cutscene("lastscene.webm")
    jump end


    

label choice3_textbad:
    l "Yes, I'm gonna text her"
    hide phoneleon1
    show textingleon at left
    "Leo: Hey, wassup. When are we meeting?"
    "Ding"
    hide textingleon
    show phoneleon1 at left
    l "OMG It's her!"
    hide phoneleon1
    show textingleon at left
    "Nadia: Heyy! I'm down for a meeting, what do you think about doing?"
    hide textingleon
    show awfulphoneleon at left
    "Leo:  Anything, I don't care. You get a reservation or something, I'm free all week."
    hide awfulphoneleon
    show annoyedleon at left
    "Nadia: Maybe this time we'll do something kinda different? Maybe go for a game billiards?"
    hide annoyedleon
    show awfulphoneleon at left
    "Leo:  Billiards sucks, you probably cannot even play and I'll have to teach you step by step haha."
    hide awfulphoneleon
    show annoyedleon at left
    stop music fadeout 3
    "Nadia: You know what? I think I don't want to go."
    hide annoyedleon
    show sadleon at left

    scene last
    with slowdissolve
    "The end"
jump end

label end:
    "The end"



    return