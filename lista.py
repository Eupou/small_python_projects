import random

is_game_over = False
words = [["t", "o", "m", "a", "t", "e"], ["c", "a", "q", "u", "i"], ["a", "b", "a", "c", "a", "x", "i"], ["a", "b", "a", "c", "a", "t", "e"],["b", "a", "n", "a", "n", "a"], ["m", "a", "ç", "a"], ["u", "v", "a"]]
number_of_attemps = 7
found_letters = []

def set_game_word():
    number_of_words = len(words) - 1
    i_word = round(random.random() * number_of_words)

    for l in words[i_word]:
        found_letters.append("_")

    return words[i_word]

game_word = set_game_word()

while(is_game_over == False):
    guessed_wrong_letter = True
    def draw_guy():
        if (number_of_attemps == 7):
            print(" ___")
            print("|")
            print("|")
            print("|")
        elif (number_of_attemps == 6):
            print(" ___")
            print("|  o")
            print("|")
            print("|")
        elif (number_of_attemps == 5):
            print(" ___")
            print("|  o")
            print("| /")
            print("|")
        elif (number_of_attemps == 4):
            print(" ___")
            print("|  o")
            print("| /|")
            print("|")
        elif (number_of_attemps == 3):
            print(" ___")
            print("|  o")
            print("| /|\\")
            print("|")
        elif (number_of_attemps == 2):
            print(" ___")
            print("|  o")
            print("| /|\\")
            print("| /")
        elif (number_of_attemps == 1):
            print(" ___")
            print("|  o")
            print("| /|\\")
            print("| / \\")

    draw_guy()

    if (number_of_attemps == 1):
        is_game_over == True
        print("GAME OVER")
        game_word_to_sting = " ".join(game_word)
        print("A palavra era: " + game_word_to_sting)
        break

    for l in found_letters:
        print(l + " ", end="")

    if (found_letters == game_word):
        print("VOCÊ VENCEU!!!")
        break
       
    aswer = input("\nguess a letter ")
    
    for letter in range(0, len(game_word)):
        if aswer == game_word[letter]:
            guessed_wrong_letter = False
            found_letters[letter] = aswer

    if guessed_wrong_letter:
        number_of_attemps -= 1
        print(number_of_attemps)