# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
word = input("Word 1: ")
anagram = input("Word 2: ")


def find_anagram(word, anagram):
    if sorted(word.lower()) == sorted(anagram.lower()):
        print("True")
    else:
        print("False")
        
find_anagram(word, anagram)
