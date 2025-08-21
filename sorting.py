import time
import sys
import random

houses = {"Gryffindor": 0.00,
          "Ravenclaw": 0.00,
          "Hufflepuff": 0.00,
          "Slytherin": 0.00
          }
school = None

def main():
        global school
        intro()
        school = choose_spawn_point()
        questions()
        result = house_calculator()
        reveal(result, school)
        play_again()

def loading(message="sorting",dots=3,delay=0.5):
    for i in range(dots):
        print(f"\r{message}{'.' * (i+1)}", end = "")
        sys.stdout.flush()
        time.sleep(delay)
        print(end = "\n")


def intro():
    time.sleep(1)
    hat_art = """                                  |--------------------------------------|
                 @@@@@@@@@@@@@    | Oh you may not think I'm pretty,     |
                 @@@*+@@@         | But don't judge on what you can see! |
                @@**++@@@@        | I'll eat myself if you can find      |
               @%=+==#@@@         | A smarter hat than me!               |
             @@@%**==**@@@       /|--------------------------------------|
             @@@@@...@@@@@      /
             @@@@@@.@@@@@@     /
            @@=+*=---@@@+@@
            @@%*@@@@@@%+#@@
           @@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@
       @@@@@-==============@@@@
   @@@@@@@@@@@@@@@======#@@@@@@@@@@@
                 @@@@@@@@
                 """

    print(hat_art)
    time.sleep(1)
    lines = [
    "Oh you may not think I'm pretty,",
    "But don't judge on what you see,",
    "I'll eat myself if you can find",
    "A smarter hat than me.\n",

    "You can keep your bowlers black,",
    "Your top hats sleek and tall,",
    "For I'm the Hogwarts Sorting Hat",
    "And I can cap them all.\n",

    "There's nothing hidden in your head",
    "The Sorting Hat can't see,",
    "So try me on and I will tell you",
    "Where you ought to be.\n",

    "You might belong in Gryffindor,",
    "Where dwell the brave at heart,",
    "Their daring, nerve, and chivalry",
    "Set Gryffindors apart;\n",

    "You might belong in Hufflepuff,",
    "Where they are just and loyal,",
    "Those patient Hufflepuffs are true",
    "And unafraid of toil;\n",

    "Or yet in wise old Ravenclaw,",
    "if you've a ready mind,",
    "Where those of wit and learning,",
    "Will always find their kind;\n",

    "Or perhaps in Slytherin",
    "You'll make your real friends,",
    "Those cunning folks use any means",
    "To achieve their ends.\n",

    "So put me on! Don't be afraid!",
    "And don't get in a flap!",
    "You're in safe hands (though I have none)",
    "For I'm a Thinking Cap!",
    "                                 ~ Harry Potter and the philosopher's stone\n"
          ]
    for line in lines:
        print(line)
        time.sleep(1)

    time.sleep(1.5)
    print("Well, well, well....another curious mind..ready to be sorted eh?\n")
    time.sleep(1.5)
    print("Before we begin, let's discover the place where your magical journey will begin!\n")
    time.sleep(2)



def choose_spawn_point():
    print("\nSo, tell me. From where do you hail?")
    print("A. Europe")
    print("B. Asia + Oceania")
    print("C. North America")
    print("D. South America")
    print("E. Africa")
    print("\nJust enter the option, no need to type the full name of the continent!" )

    ans = input("> ").strip().lower()
    if ans == "a" or ans == "a.":
        return "Hogwarts"
    elif ans == "b" or ans == "b.":
        return "Mahoutokoro"
    elif ans == "c" or ans == "c.":
        return "Ilvermorny"
    elif ans == "d" or ans == "d.":
        return "Castelobruxo"
    elif ans == "e" or ans == "e.":
        return "Ugadou"

    else:
        loading("hmm", dots = 3, delay = 0.75)
        print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option from A-E")
        time.sleep(1.25)
        return choose_spawn_point()

def update_scores(weights: dict):
    for house, points in weights.items():
        houses[house] += points

def house_calculator():
    max_score = max(houses.values())
    winners = [h for h, score in houses.items() if score == max_score]
    if len(winners) == 1:
        return winners[0]
    else:
        return tiebreaker(winners)

def tiebreaker(candidates: list):
    loading("Hmm", dots = 3, delay = 0.75)
    print("Oh my! A Hatstall, its been a long time, how curious.......")
    time.sleep(1)
    print("Let's see....one more question.....yes, that should settle it")
    loading(".", dots = 2, delay = 0.75)
    while True:
        print("Q Tie-breaker. What are you most looking forward to learning at Hogwarts?\n")
        print("A. Apparition and Disapparition (being able to materialize and dematerialize at will)\n")
        print("B. Transfiguration (turning one object into another object)\n")
        print("C. Flying on a broomstick\n")
        print("D. Hexes and jinxes\n")
        print("E. All about magical creatures, and how to befriend/care for them")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.19, "Ravenclaw": 0.6, "Hufflepuff": 0.9, "Slytherin": 0.23})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.09, "Ravenclaw": 0.27, "Hufflepuff": 0.13, "Slytherin": 0.12})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.19, "Ravenclaw": 0.07, "Hufflepuff": 0.18, "Slytherin": 0.09})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.10, "Ravenclaw": 0.11, "Hufflepuff": 0.13, "Slytherin": 0.28})
            break
        elif ans in ["e", "e."]:
            update_scores({"Gryffindor": 0.34, "Ravenclaw": 0.49, "Hufflepuff": 0.47, "Slytherin": 0.28})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A, B, C, D or E\n")
            continue
    return house_calculator()


def questions():
    hat_image = r"""

                    &&&&&X:
                     X&$$$$$$&&$$X+
                      ;&$$$$$$$$$$$&;
                         ;&$$$$$$$$$$$&;
                          .&&$$$$$$$$$$&$
                          .&$$$$$$$$$$$$$$
                           +&$$$$$$$$$$$$&:
                          .&$$$$$$$$$$$$$$$
                          ;&$$$$$$$$$$XX$$&.
                      .   +&$X$$X$$XXXXXXX$&.
                      . . $$X$X$XXXX$XXXXXX$& .
                        X&$$$$$$$$$$$$$$$$$$$
                       ;&;X$$$$+$&$$$$$$$$$$X
                 :;+XX$&x;$$$$x;+$$$xxXXXXX;+&
           .+&&&$$$$$$$$$$$$$&$+X$$&&$$$;;$;+&
         +&&&&&&&&&&&&$$$$$$$$$$$$$&&X$XX$&&$$&&X
         .$&$$$$$$$$$$$$$&&&$$$$$$$$$$$$$$$$$$$$$$&&+
            :X&&&$$$$$$$$$$&&&&$$$$$$$$$$$$$$$$$$$$$$$&X:
                   ::::.        :X$&&$$$$$$&&&&&&&&&&&&&&&X.
                                               +&&&&&&&&&X.

          ___ ___ .  __      __   ___ ___     __  ___       __  ___  ___  __
    |    |__   |  ' /__`    / _` |__   |     /__`  |   /\  |__)  |  |__  |  |
    |___ |___  |    .__/    \__> |___  |     .__/  |  /~~\ |  \  |  |___ |__/

     __                               ___  __
    /__` |__|  /\  |    |       |  | |__    _|
    .__/ |  | /~~\ |___ |___    |/\| |___  |
                                           .                                         """
    loading(".", dots = 3, delay = 0.4)
    print("Now, now, these questions are simple enough, even for those with the mind of trolls! Answer these so I uncover the fog in you mind!")
    time.sleep(1.5)
    print(hat_image)
    loading("loading", dots = 2, delay = 0.5)
    first_question_list = [q1, q2, q3]
    random.shuffle(first_question_list)
    for q in first_question_list:
        q()

    loading(dots = 4, delay = 0.4)
    print("Hmmmmm....intresting, very intresting; now lets dive deeper into your brain shall we?")
    loading(".", dots = 4, delay = 0.5)
    second_question_list = [q4, q5]
    random.shuffle(second_question_list)
    for q in second_question_list:
        q()
    loading(dots = 4, delay = 0.4)
    print("hmmmmm.....yes.. it is all coming in nicely, lets carry on")
    loading(".", dots = 4, delay = 0.5)
    third_question_list = [q6, q7, q8, q9, q10, q11]
    random.shuffle(third_question_list)
    for q in third_question_list:
        q()
    loading(dots = 4, delay = 0.4)
    print("Ah, I see its so clear now, just a little bit more and You will soon find your kind!")
    loading(".", dots = 4, delay = 0.5)
    fourth_question_list = [q12, q13, q14]
    random.shuffle(fourth_question_list)
    for q in fourth_question_list:
        q()
    loading(dots = 4, delay = 0.4)
    print("Hmmmm......what do I sense? I am not sure perhaps one more question? yes, one more question will do!")
    loading(".", dots = 4, delay = 0.5)
    q15()

def q1():
    while True:
        print("Q. What do you prefer more?")
        print("A. Dawn")
        print("B. Dusk\n")
        ans1 = input(">").strip().lower()
        if ans1 in ["a", "a."]:
            update_scores({"Gryffindor": 0.73, "Ravenclaw": 0.73, "Hufflepuff": 0.30, "Slytherin": 0.26})
            break
        elif ans1 in ["b", "b."]:
            update_scores({"Gryffindor": 0.27, "Ravenclaw": 0.27, "Hufflepuff": 0.70, "Slytherin": 0.74})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A or B\n")
            time.sleep(1.75)
            continue

def q2():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. Where would you like to spend your time?")
        print("A. In a forest")
        print("B. Near a lake")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.74, "Ravenclaw": 0.73, "Hufflepuff": 0.26, "Slytherin": 0.28})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.27, "Ravenclaw": 0.27, "Hufflepuff": 0.70, "Slytherin": 0.74})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A or B\n")
            continue

def q3():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. Which one will you choose?")
        print("A. Moon")
        print("B. Stars")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.27, "Ravenclaw": 0.74, "Hufflepuff": 0.33, "Slytherin": 0.72})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.73, "Ravenclaw": 0.26, "Hufflepuff": 0.64, "Slytherin": 0.28})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A or B\n")
            continue

def q4():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. Which colour do you like more?")
        print("A. Black")
        print("B. White")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.27, "Ravenclaw": 0.74, "Hufflepuff": 0.33, "Slytherin": 0.72})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.73, "Ravenclaw": 0.26, "Hufflepuff": 0.64, "Slytherin": 0.28})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A or B\n")
            continue

def q5():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. Four boxes are placed before you. Which would you try and open?\n")
        print("A. The small tortoiseshell box, embellished with gold, inside which some small creature seems to be squeaking.\n")
        print("B. The gleaming jet black box with a silver lock and key, marked with a mysterious rune that you know to be the mark of Merlin.\n")
        print("C. The ornate golden casket, standing on clawed feet, whose inscription warns that both secret knowledge and unbearable temptation lie within.\n")
        print("D. The small pewter box, unassuming and plain, with a scratched message upon it that reads ‘I open only for the worthy.")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.14, "Ravenclaw": 0.18, "Hufflepuff": 0.46, "Slytherin": 0.18})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.20, "Hufflepuff": 0.16, "Slytherin": 0.46})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.19, "Ravenclaw": 0.44, "Hufflepuff": 0.21, "Slytherin": 0.19})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.49, "Ravenclaw": 0.19, "Hufflepuff": 0.17, "Slytherin": 0.17})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q6():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. You and two friends need to cross a bridge guarded by a river troll who insists on fighting one of you before he will let all of you pass. Do you:\n")
        print("A. Attempt to confuse the troll into letting all three of you pass without fighting?\n")
        print("B. Suggest drawing lots to decide which of you will fight?\n")
        print("C. Suggest that all three of you should fight (without telling the troll)?\n")
        print("D. Volunteer to fight?")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.20, "Ravenclaw": 0.44, "Hufflepuff": 0.18, "Slytherin": 0.23})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.16, "Ravenclaw": 0.17, "Hufflepuff": 0.47, "Slytherin": 0.17})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.19, "Hufflepuff": 0.16, "Slytherin": 0.42})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.46, "Ravenclaw": 0.19, "Hufflepuff": 0.19, "Slytherin": 0.18})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q7():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. If it lured you, it would smell of:\n")
        print("A. A crackling log fire")
        print("B. The sea")
        print("C. Fresh parchment")
        print("D. Home")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.44, "Ravenclaw": 0.17, "Hufflepuff": 0.16, "Slytherin": 0.21})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.21, "Ravenclaw": 0.22, "Hufflepuff": 0.18, "Slytherin": 0.46})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.16, "Ravenclaw": 0.45, "Hufflepuff": 0.22, "Slytherin": 0.15})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.19, "Ravenclaw": 0.15, "Hufflepuff": 0.42, "Slytherin": 0.18})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q8():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. One of your house mates has cheated in a Hogwarts exam by using a Self-Spelling Quill. Now he has come top of the class in Charms, beating you into second place. Professor Flitwick is suspicious of what happened. He draws you to one side after his lesson and asks you whether or not your classmate used a forbidden quill. What do you do?\n")
        print("A. Lie and say you don’t know (but hope that somebody else tells Professor Flitwick the truth)\n")
        print("B. Tell Professor Flitwick that he ought to ask your classmate (and resolve to tell your classmate that if he doesn’t tell the truth, you will).\n")
        print("C. Tell Professor Flitwick the truth. If your classmate is prepared to win by cheating, he deserves to be found out. Also, as you are both in the same house, any points he loses will be regained by you, for coming first in his place.\n")
        print("D. You would not wait to be asked to tell Professor Flitwick the truth. If you knew that somebody was using a forbidden quill, you would tell the teacher before the exam started.")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.17, "Ravenclaw": 0.14, "Hufflepuff": 0.43, "Slytherin": 0.18})
            loading("Thinking", dots = 3, delay = 0.5)
            print("won't tell your professor will you? You are one of the loyal lot, then.")
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.43, "Ravenclaw": 0.16, "Hufflepuff": 0.22, "Slytherin": 0.14})
            loading("Thinking", dots = 3, delay = 0.5)
            print("trying to play both sides, eh? either be brave and resolve the whole mater or be brave and loose the trust of both? How curious!")
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.22, "Ravenclaw": 0.45, "Hufflepuff": 0.16, "Slytherin": 0.19})
            loading("Thinking", dots = 3, delay = 0.5)
            print("nice! I like the way your mind is thinking! secretly betray your friend without them knowing and making up for all they loose, you are not a troll-mind afterall!")
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.25, "Hufflepuff": 0.19, "Slytherin": 0.49})
            loading("Thinking", dots = 3, delay = 0.5)
            print("You don't play nice eh? You wouldnt loose an opportunity to get ahead, how ambitious, how interesting!")
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You think you can get away by just running? Wrong! Now professor Fitwick is disappointed! If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q9():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. Which of the following do you find most difficult to deal with?\n")
        print("A. Hunger")
        print("B. Cold")
        print("C. Loneliness")
        print("D. Boredom")
        print("E. Being Ignored")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.10, "Ravenclaw": 0.29, "Hufflepuff": 0.28, "Slytherin": 0.10})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.14, "Ravenclaw": 0.14, "Hufflepuff": 0.25, "Slytherin": 0.26})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.32, "Ravenclaw": 0.13, "Hufflepuff": 0.24, "Slytherin": 0.09})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.32, "Ravenclaw": 0.13, "Hufflepuff": 0.10, "Slytherin": 0.28})
            break
        elif ans in ["e", "e."]:
            update_scores({"Gryffindor": 0.11, "Ravenclaw": 0.32, "Hufflepuff": 0.12, "Slytherin": 0.27})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A, B, C, D or E\n")
            continue

def q10():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. You enter an enchanted garden. What would you be most curious to examine first?\n")
        print("A. The silver leafed tree bearing golden apples\n")
        print("B. The fat red toadstools that appear to be talking to each other\n")
        print("C. The bubbling pool, in the depths of which something luminous is swirling\n")
        print("D. The statue of an old wizard with a strangely twinkling eye")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.17, "Ravenclaw": 0.45, "Hufflepuff": 0.18, "Slytherin": 0.16})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.25, "Hufflepuff": 0.42, "Slytherin": 0.17})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.16, "Ravenclaw": 0.26, "Hufflepuff": 0.21, "Slytherin": 0.46})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.49, "Ravenclaw": 0.18, "Hufflepuff": 0.19, "Slytherin": 0.21})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, don't like gardens, eh? If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q11():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. What kind of instrument most pleases your ear?\n")
        print("A. The violin")
        print("B. The trumpet")
        print("C. The piano")
        print("D. The drum")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.17, "Ravenclaw": 0.20, "Hufflepuff": 0.20, "Slytherin": 0.48})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.17, "Hufflepuff": 0.44, "Slytherin": 0.18})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.21, "Ravenclaw": 0.46, "Hufflepuff": 0.19, "Slytherin": 0.18})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.44, "Ravenclaw": 0.17, "Hufflepuff": 0.17, "Slytherin": 0.16})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't like music huh? Well atleast choose the instrument you like more! If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q12():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. After you have died, what would you most like people to do when they hear your name?\n")
        print("A. Miss you, but smile")
        print("B. Ask for more stories about your adventures")
        print("C. Think with admiration of your achievements")
        print("D. I don't care what people think of mw after I'm dead; It's what they think while I'm alive that counts")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.16, "Hufflepuff": 0.42, "Slytherin": 0.19})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.46, "Ravenclaw": 0.19, "Hufflepuff": 0.14, "Slytherin": 0.19})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.45, "Hufflepuff": 0.22, "Slytherin": 0.17})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.20, "Hufflepuff": 0.22, "Slytherin": 0.45})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You think you won't die? Who are you, Voldemort? If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q13():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. A Muggle confronts you and says that they are sure you are a witch or wizard. Do you:\n")
        print("A. Ask what makes them think so?\n")
        print("B. Agree, and ask whether they’d like a free sample of a jinx?\n")
        print("C. Agree, and walk away, leaving them to wonder whether you are bluffing?\n")
        print("D. Tell them that you are worried about their mental health, and offer to call a doctor.")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.17, "Ravenclaw": 0.45, "Hufflepuff": 0.20, "Slytherin": 0.17})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.21, "Ravenclaw": 0.17, "Hufflepuff": 0.20, "Slytherin": 0.41})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.47, "Ravenclaw": 0.21, "Hufflepuff": 0.15, "Slytherin": 0.23})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.16, "Ravenclaw": 0.17, "Hufflepuff": 0.45, "Slytherin": 0.20})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You can't run away! The muggle will be even more skecptical now! If you wish to continue, enter just the option A, B, C or D\n")
            continue

def q14():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. Which nightmare would frighten you most?\n")
        print("A. Standing on top of something very high and realizing suddenly that there are no hand- or footholds, nor any barrier to stop you falling.\n")
        print("B. An eye at the keyhole of the dark, windowless room in which you are locked.\n")
        print("C. Waking up to find that neither your friends nor your family have any idea who you are.\n")
        print("D. Being forced to speak in such a silly voice that hardly anyone can understand you, and everyone laughs at you.")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.20, "Ravenclaw": 0.46, "Hufflepuff": 0.18, "Slytherin": 0.20})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.45, "Ravenclaw": 0.18, "Hufflepuff": 0.17, "Slytherin": 0.18})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.17, "Ravenclaw": 0.15, "Hufflepuff": 0.45, "Slytherin": 0.15})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.18, "Ravenclaw": 0.21, "Hufflepuff": 0.20, "Slytherin": 0.47})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A, B, C or D\n")
            continue
def q15():
    loading("sorting", dots = 2, delay = 0.5)
    while True:
        print("Q. How would you like to be known to history?\n")
        print("A. The Wise")
        print("B. The Good")
        print("C. The Great")
        print("D. The Bold")
        ans = input(">").strip().lower()
        if ans in ["a", "a."]:
            update_scores({"Gryffindor": 0.19, "Ravenclaw": 0.46, "Hufflepuff": 0.19, "Slytherin": 0.16})
            break
        elif ans in ["b", "b."]:
            update_scores({"Gryffindor": 0.17, "Ravenclaw": 0.16, "Hufflepuff": 0.44, "Slytherin": 0.17})
            break
        elif ans in ["c", "c."]:
            update_scores({"Gryffindor": 0.20, "Ravenclaw": 0.22, "Hufflepuff": 0.20, "Slytherin": 0.44})
            break
        elif ans in ["d", "d."]:
            update_scores({"Gryffindor": 0.44, "Ravenclaw": 0.17, "Hufflepuff": 0.16, "Slytherin": 0.23})
            break
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("\nHmmmm....intresting, You don't abide by the rules do you? If you wish to continue, enter just the option A, B, C or D\n")
            continue



def reveal(house: str, school: str):
    loading("deciding", dots = 5, delay = 1)
    print("Yes....yes, I have decided you house!")
    if school != "Hogwarts":
        print(f"Hogwarts, is a bit far, why dont you try {school}? it is the closest school from where you live!")
    print(f"You belong to {house} at {school}")

    if house == "Gryffindor":
        logo = r"""

                   ...:--.=%*..
                 ...:+#%%%%%%%+..
                .=%%%%%%%%%%%%%%%*:.
               .*%%%%%%%%%%%%%%%%%%%%%*.
              .=%%%%%%%%%%%%%%%%%%%%%%*.      ..
             ..%%%%%%%%%%%%%%%%%%+*%%#.     .*%%:.
             .*%%%%%%%%%%%%%%%%%%...-.     *%%%%*.
             -%%%%%%%%%%%%%%%%%%%%%%#-.. ..%%%%%*.
            .#%%%%%%%%%%%%%%%%%%%%%%%%.. .-%%%%-.
            ..%%%%%%%%%%%%%%%%%%%=-+-.  .:%%%%%.
             .=%%%%%%%%%%%%%%%%%%%%%%*...=%%%%-.
              .+*%%%%%%%%%%%%%%%%%%%%%=:-%%%%=
  ...=-..        :%%%%%%%%%%%%%%%%%%%%%%%%%%%.
.*#*%%%%=..      ..%%%%%%%%%%%%%%%%%%%%%%%%%*.
.%%%*....#..      ..#%%%%%%%%%%%%%%%%%%%%%%%:.
:%#..    .*:         #%%%%%%%%%%%%%%%%%%%%%=.
.#..      .%-        .%%%%%%%%%%%%%%%%%%%%%%%%%#*...
 .         +%.        +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=...
           =%..       =%%%%%%%%%%%%%%%%%%%=---#%%%%%%%%=.
           =%:.       +%%%%%%%%%%%%%%%%%+      .%%%%%%%:.
           =%-.      .#%%%%%%%%%%%%%%%%-.       ......
           =%+.      =%%%%%%%%%%%%%%%%..
           =%*.    ..%%%%%%%%%%%%%%%+.
           =%#.   ..%%%%%%%%%%%%%%#..
           =%%.   .%%%%%%%%%%%%%%%:.
           .%%-. .=%%%%%%%%%%%%%%%*.
           .-%%:..%%%%%%%%%%%%%%%%%*.
            .*%%%%%%%%%%%%%%%%%%%%%%..
             .:***%%%%%%%%%%%%%%%%%%%.
                 .%%%%%%%%%%%%%%%%%%%.
                .:%%%%%%+-%%%%%%%%%%+.
                .%%%%%%*. ...%%%%%%%..
               .-%%%%%%.   ..#%%%%%*..
               ..=%%%%+.   ..+%%%%%#..
                 .*%%%=.     ..=%%%%#..
                 .-%%%%:        .*%%%%%-..
                 .:%%%%%%:..      -%%%%%%%-..
                  ..%%%%%%%-.     ..=%%%%%%:.
                     ..=+=:..        ....
                                            """
        print(logo)

    elif house == "Ravenclaw":
        logo = r"""
                           .... .. ..
                   ..%=..  .=.
                    .:%:.. .%.
                    ..%%...+%=
                     .#%...#%+ ...
                     .%%:.+%%. .=.
                    .:%%-.%%+..#=.
                   ..*%%:%%%.-%%..
                   .-%%%%%%*%%%=....
                 ..:%%%%%%%%%%=..*..
                 ..%%%%%%%%%%..:%*.
                ..*%%%%%%%%%%%%%%...
               ..+%%%%%%%%%%%%%#.#:.
               .:%%%%%%%%%%%%%#%%...
              ..#%%%%%%%%%%%%%%#....
              .:%%%%%%%%%%%%%%==#%...
              .*%%%%%%%%%%%%%%%%%...
              .#%%%%%%%%%%%%%%%%%%-.
              .*%%%%%%%%%%%%%%%%%%.
              .=%%%%%%%%%%%%%%%%%%...
              .:%%%%%%%%%%%%%%%%%%..
              ..%%%%%%%%%%%%%%%%%%-..
              ..%%%%%%%%%%%%%%%%%%%.
               .#%%%%%%%%%%%%%%%%%%:.
               .#%%%%%%%%%%%%%%%%%%-.
               .+%%%%%%%%%%%%%%%%%%:.
               .:%%%%%%%%%%%%%%%%#+-.
      ...........%%%%%%%%%%%%%%%%#....
      ..=#%%%%%+*%%%%%%%%%%%%%%%%#-..
    ..*%%%%%%%%%%%%%%%%%%%%%%%%%%%=..
    .#%%%%%%%%%%%%%%%%%%%%%%%%%+-...
   .:%%-.....*%%%%%%%%%%%%%%#*+:..
    .:..    ..:%%%%%%%%%%%%%%%*...
              ..=%%%%%%%%%%%%%%%%-..
              ....%%%%%%%%%%%%%%%%%*.... .
                 .+%%%%%%%%%%%%%%%%%%%*-.........
                 .+%%%%%%%%=...*%%%%%%%%%%%%%%%:.
          .......:%%%%%%%%-. ....:#%%%%%%%%%%*...
        ..+##:.-%%%%%%=:....     ...:*%*++-:...
          ..++#%%-#%..               .......
          ..:+=+%%%*.
             .....+%.
            .    ....                                    """
        print(logo)

    elif house == "Hufflepuff":
        logo = r"""



             +@@@@+. #@@%.
            .@@@@@@@@@@@*-:.
             =@@@@@@@@@*=. :*-..
           .-@@@@@@@@%-=@@@+....==@@*
           :%@@@@@@*:.....::=*%%#.@@+
           #@@@@#:.              :%-.
          :@@@@=.    -++++****+=-.
          -@@@*         :*.
          :@@@=.:       *@=.
          .@@@#@#       =@@@@%*++++***###*=-..
           #@@@@#       .*@@@@@@@@@@@@@@@@@@@@@%-.
           -@@@@@=%.      .+@@@@@@@@@@@@@@@@@@@@@@@*.
         .%%%@@@@@@%.  -#..+@@@@@@@@@@@@@@@@@@@@@@@@@@+.
       .*@@@+@@@@@@@@*..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
    .-%@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
 .-#@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=
-@@@@@@@@@%*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@.
@@@@@@#-.*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*%@@@@=
-@@@#.=@@@@@@@@@@@@*=:-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+@@@@+
  ..+@@@@@@@*=-:..      .:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@:-@@@@@*#-
   +@@@@@-.                 .:=*@@@@@@@@@@@@@@@@@@@@@@-. -@@@@@@*
   :@@@@*                       .=%#**%@@@@@@@@@@@@@=.    .:+**-.
     .::.                     ..:::+%@@+#@@@@@@@@@+.
                          .:@@@@@@@@@@@@@#@@@@@@@-
                          :%@@@@@@@@@@#+@@@@@@@@@.
                          .:@@*.  ..:%@@@@@@@@@@+
                                   :@@@@@@@#:...
                                   %@@@@#:.
                                   *@@@@+
                                   .-##+.

                                                                 """
        print(logo)

    elif house == "Slytherin":
        logo = r'''


                     .........
             .......:=*#%%@%#+-......
          ....:*%%%%%%%%%%%%%%%%%#-...         ....
          ..:#%%%%%%%%%%%%%%%%%%%%%%-.         .:..
        ...-%%%%%%%%%%%%%%%%%%%%%%%%%:.     ...+:..
        ..=%%%%%%%%%%%%%%%%%%%%%%%%%%@:.  ....#-.
        .=%%%%%%%%*%%%%=%%%%%%%%%%%%%%+.  ..-%*.
      ..=%%%%%%%%*%%%%+*..:#%%%%%%%%%%+....=%%+..
     ..-%%%%%%%%%%%*-:..  ..*%%%%%%%%%+...+%%%+..
     .:%%%%%%%%%*%:.-...  ..=%%%%%%%%%+...#%%%%..
     ...=%%%%+-#-.-=....  ..%%%%%%%%%%:...#%%%%#..
          ...:#--*-..   ...%%%%%%%%%%*....=%%%%%=..
          ..-:.......  ...#%%%%%%%%%#......#%%%%%=....
          .:=..       ..-%%%%%%%%%%%:..   ..*%%%%@=...
          ....      ...*%%%%%%%%%%%..     ...*%%%%%#...
                  ...:#%%%%%%%%%%@: .     ....+%%%%%#....
                  ..=%%%%%%%%%%%#..       .....+%%%%%%-..
                ...*%%%%%%%%%%@+. .  .. ........+%%%%%%-..
                ..#%%%%%%%%%%@:.....-*##%%%%%%%#-%%%%%%%-..
               .:%%%%%%%%%%%*...=#%%%%%%%%%%%%%%%=%%%%%%%..
             ..-%%%%%%%%%%%:.:#%%%%%%%%%%%%%%%%%%-%%%%%%%+.
          ....=%%%%%%%%%%%..%%%%%%%%%%%%%%%%%%%%%-%%%%%%%#.
          ...+%%%%%%%%%%*.-%%%%%%%%%%@#++*%%%%%%#+%%%%%%%*.
          ..=%%%%%%%%%%+..%%%%%%%%%%-... ...-*%*+%%%%%%%%:=..
         ..-%%%%%%%%%%+...%%%%%%%%@...........=%%%%%%%%%-#%#...
        ..:#%%%%%%%%%%....%%%%%%%%%%+:...:=#%%%%%%%%%%%:#%%%+..
        ..+%%%%%%%%%%:....=%%%%%%%%%%%%%%%%%%%%%%%%%%==%%%%%@..
        ..%%%%%%%%%%*......=%%%%%%%%%%%%%%%%%%%%%%%+-%%%%%%%@..
        .:%%%%%%%%%%+...  ..:%%%%%%%%%%%%%%%%%%%#:.%%%%%%%%%%..
        .:%%%%%%%%%%*...  .....*@%%%%%%%%%%%%*:...-%%%%%%%%%+..
        .:@%%%%%%%%%%:..        ..:-====-:.... ...#%%%%%%%%%:.
        ..#%%%%%%%%%%%..        . ....... ......:%%%%%%%%%%=..
        ..-%%%%%%%%%%%%:...                  ..=%%%%%%%%%%=..
          .#%%%%%%%%%%%%=....             ....#%%%%%%%%%%+.
          ..#%%%%%%%%%%%%%=......    ......=%%%%%%%%%%%%-..
          ...#%%%%%%%%%%%%%%#-.........:=%%%%%%%%%%%%%#....
            ..+%%%%%%%%%%%%%%%%%%@%@@%%%%%%%%%%%%%%%%=...
            ...:%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@=.....
             ....-#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#-....
                 ...+%%%%%%%%%%%%%%%%%%%%%%%%#=....
                     ..-#%%%%%%%%%%%%@%%%*-.....
                     ..........::::..........


                                                                 '''
        print(logo)

    school_tidbit(school)
    print("good luck in your magical journey!\n")





def school_tidbit(place):
    if place == "Ilvermorny":
        print("Funfact: Ilvermorny school of Witchcraft and wizardry is located in mount greylock, Massachussets, which is around 150 miles from Harvard University!")
    elif place == "Mahoutokoro":
        print("Funfact: Mahoutokoro is one of the smallest wizarding schools out there, It is the school which gave world, Quidditch. The school is located in Japan, on top of a volcanic island!")
    elif place == "Ugadou":
        print("Funfact: Ugadou is situated in Uganda, Africa and is particularly famous for its wandless magic!")
    elif place == "Castelobruxo":
        print("Funfact: Castelobruxo is situated in Brazil, deep within Amazon rainforest, is the only south american wizarding school out there!")
    else:
        print("Funfact Hogwarts is situated in scotland and was founded in 990AD!")


def play_again():
    while True:
        print("Do you wish to be sorted again? just reply in yes or no")
        ans = input(">").lower().strip()
        if ans in ["yes", "y", "y.", "yes.", "yup", "yup."]:
            time.sleep(1)
            print("Well let's sort you again, I hope you can bear my song once again.\n")
            main()
        elif ans in ["no", "nope", "n.", "no.", "nope."]:
            time.sleep(1)
            print("No worries, You know where I rest, you can always approach me, If ever in doubt about your house!")
            sys.exit(0)
        else:
            loading("hmm", dots = 3, delay = 0.75)
            print("Hmmmmm......still can't understand you, can you say it in just yes/no?\n")



if __name__ == "__main__":
    main()
