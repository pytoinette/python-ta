import sys
import os


def palindrome(s):
    small_word = s.upper()
    no_space_word = small_word.replace(' ' , '')
    reverse = no_space_word[::-1]

#    if no_space_word == reverse:
  #      print(f"{s} is a palindrome")
  # else:
    #    print(f"{s} is not a palindrome")
        
    return no_space_word == reverse
        
def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))





