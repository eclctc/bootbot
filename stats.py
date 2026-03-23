from collections import Counter

def count_words(text):
    count = 0
    words = text.split()
    count = [word for word in words]
    
    return len(count)

def count_characters(text):
    characters = {}
    # Loop through the text by character and add counts to the dictionary
    for char in text.lower():
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    
    return characters


def sort_characters(characters):
    char_data = [{"char": k, "num": v} for k, v in characters.items()]
    sorted_data = sorted(char_data, key=lambda x: x["num"], reverse=True)

    return sorted_data
    