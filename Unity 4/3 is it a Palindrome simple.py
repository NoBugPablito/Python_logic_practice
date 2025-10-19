def palindrome(word):
    reverse_word = word[::-1]
    status = 1
    if(word != reverse_word):
        status = 0 
    return status

word = input("Enter a word ")
status = palindrome(word)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! Nice try")
