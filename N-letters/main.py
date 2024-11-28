def interactive_word_base():
    words = ["yoda", "best", "has"]
    
    print("Your initial words:", words)
    print("Commands:")
    print(" - add <word>: Add a new word to the base")
    print(" - list: Show all words in the base")
    print(" - concat: Construct a string using letter of each word")

    while True:
        command = input("> ").strip()
        parts = command.split(" ", 1) 

        if parts[0] == "add" and len(parts) == 2:
            word = parts[1]
            if word in words:
                print(f"The word '{word}' already exists.")
            else:
                words.append(word)
                print(f"The word '{word}' has been added.")
        
        elif parts[0] == "list":
            print("Current words in the base:", words)
        
        elif parts[0] == "concat":
            letters = []

            for i, word in enumerate(words):
                if(len(word) < i ):
                    continue
                letter_number = word[i]
                letters.append(letter_number)

            result = ''.join(letters)
            print("Constructed string:", result)

        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    interactive_word_base()
