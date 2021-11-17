import time
import random


def pp(text):
    print(text)
    time.sleep(0)


def logo():
    print(
        " ___     ____  ______  ____  ____    ____      ___     ____  __ __ "
    )
    print(
        "|   l   /    ||      ||    ||    l  /    |    |   l   /    ||  |  |"
    )
    print(
        "|    l |  o  ||      | |  | |  _  ||   __|    |    l |  o  ||  |  |"
    )
    print(
        "|  D  ||     ||_|  |_| |  | |  |  ||  |  |    |  D  ||     ||  ~  |"
    )
    print(
        "|     ||  _  |  |  |   |  | |  |  ||  |_ |    |     ||  _  ||___, |"
    )
    print(
        "|     ||  |  |  |  |   |  | |  |  ||     |    |     ||  |  ||     |"
    )
    print(
        "|_____||__|__|  |__|  |____||__|__||___,_|    |_____||__|__||____/ "
    )


def name():
    name = random.choice(["Bella", "Lucy", "Addison", "Olivia", "Emma",
                          "Eva", "Sophia", "Aria", "Mia", "Ella", "Luna"])
    return name


def Gold(x):
    if x <= 20:
        gold = random.randint(19, 21)
    else:
        gold = random.randint(21, x+5)
    return gold


def prof():
    pro = random.choice(["Physical Therapist", "Interior Designer", "Founder",
                         "Communications", "Teacher", "College Student",
                         "Pharmacist", "Model", "Nurse",
                         "Social Media Manager"])
    return pro


def again():
    while True:
        x = input("Game Over\nDo want play agian? y/n\n").lower()
        if x == 'y':
            game()
        elif x == 'n':
            pp("Thank you")
            exit()
        else:
            pp("Sorry?")


def lecture(bag, money, p, c):
    while True:
        if "level_3" in c:
            pp("You have already Super brain\n")
            start(bag, money, p, c)
        else:
            print("You have", money, "$")
            pp("")
            x = input("One lecture has 30 dollar do you confirm?"
                      " y/n\n").lower()
            if x == 'y':
                if money >= 30:
                    print("-30$")
                    pp("")
                    money -= 30
                    print("You have now", money, "$")
                    pp("")
                    if "level_2" in c:
                        c.append("level_3")
                        pp("You have level 3")
                        pp("Graduated\n")
                        p += 5
                        start(bag, money, p, c)
                    elif "level_1" in c:
                        c.append("level_2")
                        pp("You have level 2\n")
                        p += 4
                        start(bag, money, p, c)
                    else:
                        c.append("level_1")
                        pp("You have level 1\n")
                        p += 3
                        start(bag, money, p, c)
                else:
                    pp("Sorry your money is so less\n")
                    start(bag, money, p, c)
            elif x == 'n':
                start(bag, money, p, c)
            else:
                pp("sorry?")


def well(bag, money, p, c):
    while True:
        if "Beauty" in c:
            pp("You have already Cool guy\n")
            start(bag, money, p, c)
        else:
            print("You have", money, "$")
            pp("")
            x = input("One entry has 30 dollar do you confirm? y/n\n").lower()
            if x == 'y':
                if money >= 30:
                    pp("-30$")
                    money -= 30
                    print("You have now", money, "$")
                    pp("")
                    if "Body" in c:
                        c.append("Beauty")
                        pp("You have Beauty face\n")
                        p += 5
                        start(bag, money, p, c)
                    elif "Fashion" in c:
                        c.append("Body")
                        pp("You have Perfect body\n")
                        p += 4
                        start(bag, money, p, c)
                    else:
                        c.append("Fashion")
                        pp("You have Fashion styles\n")
                        p += 3
                        start(bag, money, p, c)
                else:
                    pp("Sorry your money is so less\n")
                    start(bag, money, p, c)
            elif x == 'n':
                start(bag, money, p, c)
            else:
                pp("sorry?")


def shop(bag, money, p, c):
    pp("Welcome 'BMJ' Shopping center")
    while True:
        print("1-FLower (10$)\n2-Ring (50$)\n3-Dres (40$)\n4-Perfume (30$)+\
            \n5-Notebook (20$)\n6-Teddy bear (30$)\n7-Scarf (30$)\n8-Exit+\
            \nYou have", money, "$")
        pp("")
        go = input("Please enter above number\n")
        if go.isdigit() is True:
            if go == '1':
                if money >= 10:
                    bag.append("Flower")
                    pp("You bought Flower\n")
                    p += 1
                    money -= 10
                else:
                    pp("Money was weak\n")
            elif go == '2':
                if money >= 50:
                    bag.append("Ring")
                    pp("You bought Ring\n")
                    p += 4
                    money -= 50
                else:
                    pp("Money was weak\n")
            elif go == '3':
                if money >= 40:
                    bag.append("Dres")
                    pp("You bought Dres\n")
                    p += 3
                    money -= 40
                else:
                    pp("Money was weak\n")
            elif go == '4':
                if money >= 30:
                    bag.append("Perfume")
                    pp("You bought Perfume\n")
                    p += 3
                    money -= 30
                else:
                    pp("Money was weak\n")
            elif go == '5':
                if money >= 20:
                    bag.append("Notebook")
                    pp("You bought Notebook\n")
                    p += 2
                    money -= 20
                else:
                    pp("Money was weak\n")
            elif go == '6':
                if money >= 30:
                    bag.append("Tedyy bear")
                    pp("You bought Teddy bear\n")
                    p += 2
                    money -= 30
                else:
                    pp("Money was weak\n")
            elif go == '7':
                if money >= 30:
                    bag.append("Scarf")
                    pp("You bought Scarf\n")
                    p += 3
                    money -= 30
                else:
                    pp("Money was weak\n")
            elif go == '8':
                start(bag, money, p, c)
            else:
                pp("Excuse me what do you want buy?\n")


def Cassino(bag, money, p, c):
    pp("Welcome to BMJ cassino")
    while True:
        if money >= 25:
            pp("You can play 40'%' chance game. One play 25$")
            print("You have", money, "$")
            pp("")
            go = input("Do you want to play y/n\n").lower()
            if go == 'y':
                for n in [3, 2, 1]:
                    pp(n)
                money -= 25
                play = random.choice([1, 2, 3, 4, 5])
                if play == 1 or play == 2:
                    pp("YOU WON !")
                    pp("Collected 50$\n")
                    money += 50
                else:
                    pp("YOU LOSS\n")
            elif go == 'n':
                start(bag, money, p, c)
        else:
            pp("Sorry you don't have money\n")
            start(bag, money, p, c)


def call(bag, money, p, c):
    while True:
        if "3" in c:
            pp("She is busy !\n")
            start(bag, money, p, c)
        else:
            pp("You have her number")
            x = input("Do you want call to her y/n\n").lower()
            if x == 'y':
                if "2" in c:
                    c.append("3")
                    x1 = input("--What is the happened--\n")
                    print("--", x, "ok i am busy--\n")
                    pp("")
                    p -= -5
                    start(bag, money, p, c)
                elif "1" in c:
                    c.append("2")
                    x1 = input("--Hi, nice to hear you.--\n")
                    print("--", x1, "fine, see you soon later.--\n")
                    pp("")
                    p += 2
                    start(bag, money, p, c)
                else:
                    c.append("1")
                    pp("--Hey ! I was going to call you--")
                    x1 = input("--How are you?--\n")
                    print("--", x1, "that's great see you tonight !--\n")
                    pp("")
                    p += 3
                    start(bag, money, p, c)
            elif x == 'n':
                start(bag, money, p, c)
            else:
                pp("Sorry?")


def date(bag, money, p, c):
    a = input("Are you ready to date? y/n\n").lower()
    if a == 'y':
        pp("Dating day")
        pp("You are waiting in restaurant")
        if p > 10:
            p += len(c)
            pp("She is coming")
            pp("Talking some funs and eating dinner")
            if len(c) >= 1:
                pp("You gived to him gift")
                if p >= 20:
                    if p >= 30:
                        pp("After dinner drinks some wines")
                        pp("And you lifted to him")
                        pp("--Thanks for the evening."
                           " Let's go it again soon--")
                        pp("")
                        pp("Super Finish\nGood Job")
                    else:
                        pp("She finished dinner")
                        pp("--Thank you, I enjoyed tonight."
                           " You're easy to talk to--")
                        pp("")
                        pp("You have chance next time\nNot bad")
            else:
                pp("She stopped talk")
                pp("--I had a nice time, but i don't think we're a match.--")
                pp("")
                pp("Maybe you need learn skills")
        else:
            pp("She sent you message")
            pp("--Sorry, I have another plans.--")
            pp("")
            pp("Don't play gambling !")
        again()
    elif a == 'n':
        start(bag, money, p, c)
    else:
        pp("sorry?")


def info(bag, money, p, c):
    pp("1-School can give you knowledges\n2-Wellness center can change"
       " you to cool guy\n3-You must buy to her Gift\n4-If you need money"
       ", go to casino\n5-And if you want can talk to her\n")
    start(bag, money, p, c)


def all(bag, money, p, c):
    pp("")
    print("You have", money, "$")
    pp("")
    if bag == []:
        pp("Bag is Empty\n\n")
        start(bag, money, p, c)
    else:
        print("In your bag", bag, "\n\n")
        pp("")
        start(bag, money, p, c)


def entry():
    pp('Welcome to "Dating Day"')
    boy = input("What is your name?\n")
    while True:
        old = input("How old are you?\n")
        if old.isdigit() is True:
            pp("\n")
            break
        else:
            pp("Sorry?")
    return boy, old


def intro(girl, gold, pro):
    print("Tonight you planed date with", girl)
    pp("")
    print("She is", pro)
    pp("")
    print("She has", gold, "years old")
    pp("")
    pp("You need prepare to tonight date\n")
    pp("GOOD LUCK !\n\n")


def start(bag, money, p, c):
    while True:
        pp("1-Go to Lectures\n2-Go to Wellness Center\n3-Go to Shopping"
           "Center\n4-Go to Cassino\n5-Call to her\n6-Go to 'Dating Day'"
           "\n7-Info\n8-Your bag\n")
        go = input("Please enter above number\n\n")
        if go.isdigit() is True:
            if go == '1':
                lecture(bag, money, p, c)
                break
            elif go == '2':
                well(bag, money, p, c)
                break
            elif go == '3':
                shop(bag, money, p, c)
                break
            elif go == '4':
                Cassino(bag, money, p, c)
                break
            elif go == '5':
                call(bag, money, p, c)
                break
            elif go == '6':
                date(bag, money, p, c)
                break
            elif go == '7':
                info(bag, money, p, c)
                break
            elif go == '8':
                all(bag, money, p, c)
                break
            else:
                pp("Please check again numbers\n")
        else:
            pp("Please check again numbers\n")


def game():
    p = 0
    c = []
    money = 100
    bag = []
    logo()
    boy, old = entry()
    girl = name()
    pro = prof()
    bold = int(old)
    gold = Gold(bold)
    intro(girl, gold, pro)
    start(bag, money, p, c)


if __name__ == '__main__':
    game()
