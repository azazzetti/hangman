chosen_word = input("Choose a random word: ").lower()
split_word = []
display = []
lives = 6
game_is_on = True

for _ in range(len(chosen_word)):
    display.append("_")


for char in chosen_word:
    split_word.append(char)
print(split_word)

while game_is_on:
    print(display)
    guess = input("Guess a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_is_on = False
            print("Game Over. No lives left")
        else:
            print(f"Wrong answer, you lose 1 life. Still {lives} lives")
    if "_" not in display:
        print(f"You Win. The word is {chosen_word}")
        game_is_on = False
