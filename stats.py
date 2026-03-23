
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