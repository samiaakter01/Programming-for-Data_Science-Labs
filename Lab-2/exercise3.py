# Problem 3 – Word Analyzer. 
# Ask the user to enter a word or short sentence. 
# Display the number of characters, vowels (a, e, i, o, u), and spaces. 
# Use a for loop to examine each character.


text = input("Enter a word or short sentence: ")


character_count = 0
vowel_count = 0
space_count = 0


for character in text:

    if character != " ":
        character_count = character_count + 1

    
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        vowel_count = vowel_count + 1

    
    if character == " ":
        space_count = space_count + 1

print("Number of characters:", character_count)
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)
