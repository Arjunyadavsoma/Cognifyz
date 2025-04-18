import string

def count_words(filename):
    word_count = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                
                line = line.lower()
                for p in string.punctuation:
                    line = line.replace(p, '') 

                words = line.split()

                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1

        for word in sorted(word_count.keys()):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("The file was not found. Please check the file path.")

filename = input("Enter the path to the text file: ")
count_words(filename)