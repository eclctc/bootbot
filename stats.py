
def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    
    return count

def count_characters(text):
    characters = {}
    # Loop through the text by character and add counts to the dictionary
    for char in text.lower():
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    
    return characters