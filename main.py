from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    num_chars = count_characters(text)
    sorted_data = sort_characters(num_chars)
    for item in sorted_data:
        if not item["char"].isalpha():  # If data isn't alpha numeric, don't print
            continue    
        else: 
            print(f"{item["char"]}: {item["num"]}")
    print(f"============= END ===============")

main()