def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = get_word_count(file_contents)

        char_count_dict = get_character_count(file_contents)

        char_count_dict_list = []
        for key in char_count_dict:
            if key.isalpha():
                value = char_count_dict[key]
                dict = {"char": key, "count": value}
                char_count_dict_list.append(dict)

        char_count_dict_list.sort(reverse=True, key=sort_on)

        result = f"--- Begin report of books/frankenstein.txt ---\n{
            word_count} words found in the document\n\n"

        for entry in char_count_dict_list:
            count = entry["count"]
            char = entry["char"]
            result += f"The '{char}' character was found {count} times\n"

        result += "--- End report ---"

        print(result)


def get_word_count(str):
    words = str.split()
    return len(words)


def get_character_count(str):
    char_dict = {}
    for char in str:
        char_lower = char.lower()
        if char_lower in char_dict:
            char_dict[char_lower] += 1
        else:
            char_dict[char_lower] = 1

    return char_dict


def sort_on(dict):
    return dict["count"]


main()
