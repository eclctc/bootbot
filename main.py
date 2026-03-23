from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents
    
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    num_chars = count_characters(text)
    sorted_data = sort_characters(num_chars)
    for item in sorted_data:
        if not item["char"].isalpha():
            continue    
        else: 
            print(item)
    print(f"============= END ===============")

main()