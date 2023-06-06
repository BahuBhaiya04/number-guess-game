#                                       Guess Game

# Player1 Input
print("Player1 Put Number To Be Guessed")
g_num = int(input())
print("Number Of Chances Given")
chance = int(input())

# GAME START MESSAGE
print(10 * "-", "GAME START", 10 * "-", "\nYou Got", chance, "Tries\nGOOD LUCK!!!")

# ----------------------------------Game Built-------------------------------- #
for i in range(1, chance + 1):
    print("Chance", i)
    guess = int(input())

# Win condition first
    if guess == g_num:
        print("HOORAHH!!!\nYOU WON\n In", i, "Tries\n", 10 * "-", "GAME END", 10 * "-")
        break
# last chance statement
    elif i == chance-1:
        print(10 * "-", "LAST CHANCE", 10 * "-")
# last chance program
    elif i == chance:
        if guess != g_num:
            print("You Have Used All Your Chances\nBETTER LUCK NEXT TIME\n", 10 * "-", "GAME END", 10 * "-")
        elif guess == g_num:
            print("HOORAHH!!!\nYOU WON\n In", chance, "Tries\n", 10 * "-", "GAME END", 10 * "-")

    elif guess > g_num:
        print("Wrong Guess\nTry Lower ;)")
    elif guess < g_num:
        print("Wrong Guess\nTry Higher ;)")
