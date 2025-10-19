# Write a function is_palindrome(text) that returns True if the string is a palindrome (reads the same backward), otherwise False.

def checkpalindrome(word):
    status = 1
    large = len(word)
    first_letter = 0
    last_letter = large - 1
    while first_letter < last_letter:
        if word[first_letter] == word[last_letter]:
            first_letter += 1
            last_letter -= 1
        else:
            status = 0
            break
    return int(status)

word = input("Enter the word: ")
status = checkpalindrome(word)
if status:
    print("It is a palindrome")
else:
    print("Sorry, try again ")


