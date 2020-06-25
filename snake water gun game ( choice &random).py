def computer():
    import random
    i = ["SNAKE", "WATER", "GUN"]
    res = random.choice(i)
    return res


def user():
    print("Choose one from the below:")
    print("S: SNAKE")
    print("W: WATER")
    print("G: GUN")
    a = input().capitalize()
    return a


# main menu of the game
from pygame import mixer
print("\n\n---------WELCOME TO THE GAME---------")
print("<><><><><><><><><><><><><><><><><><><>")
print("||       SNAKE     WATER   GUN      ||")
print("<><><><><><><><><><><><><><><><><><><>")
print("\nDESCRIPTION:: In this game Snake > Water , Water > Gun and Gun > Snake. WHO WILL SCORE MORE OUT OF 10 WILL BE WINNER.")
name = input("\nEnter Your Name : ").capitalize()
print("\n\n\t", name,"    VS     Computer")
print("\n")


mixer.init()
mixer.music.load('c:/Users/JATIN RATHI/Downloads/snappie.mp3')
mixer.music.play(100)
i = 0  # loop initialize
c = 0  # computer score
u = 0  # user score
d = 0  # draw
while i < 10:
    print("\n\n\t", i + 1, "th game")
    you = user()
    comp = computer()
    if comp == "SNAKE" and you == "W":
        c = c + 1
        print("COMPUTER WON")
    elif comp == "GUN" and you == "S":
        c = c + 1
        print("COMPUTER WON")
    elif comp == "WATER" and you == "G":
        c = c + 1
        print("COMPUTER WON")
    elif you == "S" and comp == "WATER":
        u = u + 1
        print("YOU WON")
    elif you == "G" and comp == "SNAKE":
        u = u + 1
        print("YOU WON")
    elif you == "W" and comp == "GUN":
        u = u + 1
        print("YOU WON")
    else:
        d = d + 1
        print("DRAW")

    i = i + 1
mixer.music.stop()

print("\tGAME ENDED")
print(" Computer's Total score is", c)
print(  name,"'s Total score is", u)
print(" Total no. of draw matches:", d)
if c > u:
    print(  name," lost!!")
    print(" Winner is Computer")
elif u > c:
    print(" Congratulations !!! you won by", u - c, "points")
else:
    print(" Game is Draw")

print("********  Coded by :    JATIN RATHI    *************")
import time

time.sleep(10)

    
