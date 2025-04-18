#Write a Python function that checks whether
#  a given string is a palindrome. A palindrome
#  is a word, phrase, or sequence that reads the
#  same backward as forward (e.g., "madam" or "racecar").

def palindrome(word):
    word=word.lower()
    word=word.replace(' ','')
    return word==word[::-1]

word=input("Enter the word,phrase or sequence to check whether its palindrome : ")
if palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
