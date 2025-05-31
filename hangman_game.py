import random

word_list = ["apple", "banana", "mango", "potato", "AX", "LV", "Rolex", "Jacob"]
words = random.choice(word_list).lower() 

display = []
for i in range(len(words)):
    display.append('_') 
print(display)

lives = 6 
game_over = False

while not game_over:
    guessed_letter = input("GUESS A LETTER: ").lower()

    for position in range(len(words)):
        letter = words[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    if guessed_letter not in words:
        lives -= 1
        print("Wrong! Lives left:", lives)
        if lives == 0:
            game_over = True
            print("You Lose!! The word was:", words)

    if '_' not in display:
        game_over = True
        print("You Win!")
