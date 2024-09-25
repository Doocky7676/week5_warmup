# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
my_text = 'abracadabra'
result = my_text
# a. Retrieve the 5th character.
print(result[4])
# b. Retrieve the second to last character.
print(result[-2])
# c. Find the first occurrence of the letter 'c'.
print(my_text.find("C"))
print(result[5])


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
my_text2 = 'abcdefghijklmnopqrstuvwxyz'
result2 = my_text2
# a. Extract the letters 'hij'.
print(result2[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(result2[0:13])
# c. Reverse the entire string using slicing.
print(result2[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
my_text3 = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
result3 = my_text3
print(result3.find('John F. Kennedy'))
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
my_text4 = "Python is fun. Fun is good. Good is subjective."
result4 = my_text4
# a. Extract the word 'subjective' without knowing its exact position.
print(result4.find('subjective'))
# b. Extract every third word.
substring = result4.find('fun. ')
substring2 = result4.find('good. ')
substring3 = result4.find('subjective.')
print(substring + substring2 + substring3)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(result4.replace("Python is fun. Fun is good. Good is subjective." , ".subjective is Good .good is Fun .fun is Python"))
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU."
lowercase_text = text.lower()
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

motto = ["Make", "haste", "slowly."]
single_string = " ".join(motto)
print("Single String:", single_string)

split_string = single_string.split('a')
print("Split String:", split_string)

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

sentence = "Life is what happens when you are busy making other plans."

sentence = sentence.replace("busy", "distracted")

sentence = sentence.replace("plans", "mistakes")

print(sentence)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

word = "Iteration"

result = word * 7

print(result)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

contains_moonlight = "moonlight" in quote

print(f"Does the quote contain 'moonlight'? {contains_moonlight}")

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".

phrase = "Supercalifragilisticexpialidocious"

num_characters = len(phrase)

count_i = phrase.count('i')

# b. Count the number of times the letter 'i' appears in the same word/phrase. 
print(f"Number of characters: {num_characters}")
print(f"Number of times 'i' appears: {count_i}")


