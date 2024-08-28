def main():
    path = "./books/frankenstein.txt"
    with open(path) as f:
        # Grab the contents of the file and put into a variable
        file_contents = f.read()

        # Grab the word count by splitting the book string and counting how many entries in the list
        word_count = len(file_contents.split())

        # First grab characters and their counts by using count_characters
        character_count_dict = count_characters(file_contents)

        # Transform dictionary into a list of objects containing the character (alpha only) and it's count
        character_count_list = convert_character_dict_to_list(character_count_dict)

        # Sort it decending
        character_count_list.sort(reverse=True, key=sort_on)

        # Pass the path, word count, and list of character objects to the report builder
        build_report(path, word_count, character_count_list)
        

def count_characters(string):
    character_dict = {}
    for character in string.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def convert_character_dict_to_list(character_dict):
    character_list = []
    for character in character_dict:
        if (character.isalpha() == False):
            continue
        character_object = {
            "character": character,
            "count": character_dict[character]
        }
        character_list.append(character_object)
    return character_list

def build_report(path, word_count, character_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for character in character_list:
        print(f"The {character['character']} character was found {character['count']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

if __name__ == "__main__":
    main()