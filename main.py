import pandas as pd

# Read the CSV file containing the NATO phonetic alphabet into a DataFrame
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary where the keys are letters and the values are the corresponding phonetic codes
phonetic_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Prompt the user to enter a word and convert the input to uppercase
user_word = input("Enter a word: ").upper()

# Create a list of phonetic codes corresponding to each letter in the input word
phonetic_list = [phonetic_dict[letter] for letter in user_word]

# Print the list of phonetic codes
print(phonetic_list)