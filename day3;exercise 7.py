#Ask the user for a word. Print the first and last characters using indexing
import sys
def main():
    word= input("Enter a word with 5 letters: ")#tested with Tisha
    print(word[0]) #T
    print(word[4]) #a
    return 0
if __name__ == '__main__':
    sys.exit(main())