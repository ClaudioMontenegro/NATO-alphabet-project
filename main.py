import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

game_is_on = True
while game_is_on:
    a_word = input("Enter a word: ").upper()
    nato_final = [nato_dict[letter] for letter in a_word]
    print(nato_final)
    if a_word == "EXIT":
        game_is_on = False
