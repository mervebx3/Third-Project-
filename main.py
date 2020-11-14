import random 
import time

# initial Setups 

print("\nWelcome to Hangman game by Merve \n")
name = input("Enter your Name: ")
print("Hello " + name + " ! Best of Luck")
time.sleep(2)
print("The game is about to start \n Let´s play Hangman!")
time.sleep(3)

def main(): 
    """ defining the Main Function with all global variablesg

    """
    global count 
    global display
    global word
    global already_guessed 
    global length 
    global play_game 
    words_to_guess = ["hallo", "test", "image", "film"]
    word = random.choice(words_to_guess)
    length = len(word)
    count =0 
    display = '_,' * length
    already_guessed= []
    play_game =""



def play_loop():
    """ a loop to re-execute the game when the first round ends 

        We use this argument to either continue the game after it is played once 
        or end it according to what the user suggest
    """
    global play_game
    play_game = input("Do you want to play again ? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game =input("Do you want to play again ? y = yes, n = no \n") 
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you for playing ! ")
        exit()


def hangman(): 
    """ Initializizing all the conditions required for the game 
    """
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: "+
    display + " Enter your guess: \n")
    guess = guess.strip()
    # strip() => Remove spaces at the beginning and at the end of the string 
    if len(guess.strip())== 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter \n")
        hangman()
    elif guess in word : 
        already_guessed.extend([guess])
        index = word.find(guess)
        print(index)
        word = word[:index] +"_," + word[index + 1:] 
        display= display[:index] + guess + display[index + 1:]
        print("The guess was right! \n Your guess = "+display + " \n")

    elif guess in already_guessed: 
        print("Try another letter \n")

    else: 
        count += 1 

        if count == 1 : 
            time.sleep(1)
            print("  _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count)+ " guesses remaining \n")
        elif count == 2: 
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. "+str(limit-count)+" guesses remaining \n")
        elif count == 3: 
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. "+str(limit-count)+" guesses remaining \n")
        elif count == 4: 
            time.sleep(4)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print(display)
            play_loop()
    if word == ' _ ' *length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()

main()

hangman()