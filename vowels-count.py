# Program to write a python function that takes a string input from the user and counts the number of vowels and consonants in the string
def vowel_count(text):
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    vowels_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():           #ignoring space,number,punctuation and checks if letter
            if char in vowels:
                vowels_count += 1
            else:
                consonant_count += 1

    print("Vowel count=", vowels_count)
    print("Consonant count=", consonant_count)

vowel_count(input("Enter a text: "))
