original_string = input("Write a sentence: ")

alternating_chars = ""

for i in range(len(original_string)):
    if i % 2 == 1:
        alternating_chars += original_string[i].upper()
    else:
        alternating_chars += original_string[i].lower()

print(f"This is your sentence with alternating upper and lower case characters: {alternating_chars}")


word_list = original_string.split()
alternating_words = ' '.join([word.upper() if i % 2 == 0 else word.lower() for i, word in enumerate(word_list)])

print(f"This is your sentence with alternating upper and lower case words: {alternating_words}")