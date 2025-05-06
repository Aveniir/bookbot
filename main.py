import sys

from stats import count_words
from stats import get_characters
from stats import char_dict

def get_book_text(filepath):
 with open(filepath) as f:
     return f.read()

def main():
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_counts = get_characters(book_text)
    sorted_chars = char_dict(char_counts)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

#Code to count the words from the book---------------------------------------
