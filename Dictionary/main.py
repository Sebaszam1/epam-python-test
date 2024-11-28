from dictionary import Dictionary

def interactive_mode():
    my_dict = Dictionary()
    print("Dictionary initialized. Enter commands to interact with it.")
    print("Commands: add <word> <definition>, find <word>, list, quit")

    while True:
        command = input("> ").strip()
        parts = command.split(" ")

        if parts[0] == "add" and len(parts) == 3:
            word, definition = parts[1], parts[2]
            my_dict.add_word(word, definition)
            print(f"The word '{word}' with the definition '{definition}' has been added.")
        
        elif parts[0] == "find" and len(parts) == 2:
            word = parts[1]
            print(my_dict.get_definitions(word))
        
        elif parts[0] == "list":
            words = my_dict.list_words()
            if words:
                print("Words in the dictionary:")
                for w in words:
                    print(f" - {w}")
            else:
                print("The dictionary is empty.")
        
        elif parts[0] == "quit":
            print("Goodbye!")
            break
        
        else:
            print("Unknown command. Remember the differents commands: ")
            print("add <word> <definition>, find <word>, list, quit")

def main():
        interactive_mode()

if __name__ == "__main__":
    main()
