import re

def main():
    print("Hello World")

    bookPath = "books/frankenstein.txt"
    
    text = get_book_text(bookPath)
    numWords = get_num_words(text)
    listOfWords = count_characters(text)


    print(f"--- Begin report of {bookPath} ---")
    print(f"Frankenstein by Mary Shelly has {numWords} words.")
    print()

    for item in listOfWords:
        if item[0].isalpha():
            print(f"The character {item[0]} was found {item[1]} times.")
    
    print()
    print("--- End of Report ---")


def get_num_words(text):
    if len(text) > 0:
        words = text.split()
        return len(words)
    else:
        return "No text found"

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    loweredString = text.lower()
    charDictionary = {}
    for char in loweredString:
        if char not in charDictionary:
            charDictionary[char] = 1
        else:
            charDictionary[char] += 1

        #sorted(d.items(), key=lambda x: x[1], reverse=True)

    return sorted(charDictionary.items(), key=lambda x:x[1], reverse=True)



main()