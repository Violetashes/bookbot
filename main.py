def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count_words("books/frankenstein.txt")
        print("\n")
        print_report(count_characters(file_contents))
        print("--- End report ---")


def count_words(filename):
    word_count = 0
    with open(filename) as f:
        for line in f:
            word_count += len(line.split())
    print(f"{word_count} words found in the document")

def count_characters(text):
    text_lower = text.lower()
    text_lower_alpha = ''.join(char for char in text_lower if char.isalpha())
    characters = {}
    for char in text_lower_alpha:
        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1
    characters_sorted = dict(sorted(characters.items(), key=lambda item:item[1], reverse=True))
    return characters_sorted

def print_report(text_dict):
    for key, value in text_dict.items():
        print(f"the {key} character was found {value} times")

main()