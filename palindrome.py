def palindrome_checker(word):
    small_word = word.lower()
    no_space_word = small_word.replace(' ' , '')
    reverse = no_space_word[::-1]

    if no_space_word == reverse:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

palindrome_checker()
