def num_of_words(text):
    words = text.split()
    return_text = f"Found {len(words)} total words"
    return return_text

def num_of_letters(text):
    num_letters = dict()
    lowercase_text = text.lower()
    for item in lowercase_text:
        if item in num_letters.keys():
            num_letters[item] += 1
        else:
            num_letters[item] = 1
    return num_letters
    
def sort_on(dict):
    return dict["num"]

def list_sorted_dicts(input_dict):
    sorted_list = list()
    for key, value in input_dict.items():
        if key.isalpha():
            sorted_list.append({"letter": key, "num": value})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list