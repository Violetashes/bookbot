from stats import num_of_words, num_of_letters, list_sorted_dicts
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    
    # Word count
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\n{num_of_words(book)}")
    
    # Character count (formatted output)
    print("--------- Character Count -------")
    letter_counts = num_of_letters(book)
    sorted_letters = list_sorted_dicts(letter_counts)
    
    for item in sorted_letters:
        print(f"{item['letter']}: {item['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()