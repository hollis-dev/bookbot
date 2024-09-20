#learn how to open a file in python
#learn about try/exceptions
#learn using with

#learn stacktrace
#learn lists and dictionaries


def word_count(file_contents):
    words = file_contents.split()

    return len(words)




def char_count(file_contents):
    lower_case_contents = file_contents.lower()
    char_count = {}
    for char in lower_case_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(dict):
    return dict["num"]

def sort_dict_to_list(chars_dict):
    sorted_list = []
    for key in chars_dict:
        sorted_list.append({"char": key, "num": chars_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    file_path = "books/frankenstein.txt"
    with open("books/frankenstein.txt", 'r') as f:
        file_contents = f.read()

    total_words = word_count(file_contents)
    total_char = char_count(file_contents)
    chars_sorted_list = sort_dict_to_list(total_char)

    print(f"--- Begin report of {file_path} ---")
    print(f"{total_words} words found in the document\n")

    for item in chars_sorted_list:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

main ()