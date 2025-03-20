"""Main module for the bookbot program."""
import sys
from stats import get_book_text, get_number_of_words, get_character_count, format_char_count

def main():
	try:
		if len(sys.argv) < 2:
			print('Usage: python3 main.py <path_to_book>')
			sys.exit(1)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		book_text = get_book_text(sys.argv[1]) # 'books/frankenstein.txt'
		num_words = get_number_of_words(book_text)
		print(f"Found {num_words} total words")
		char_count = get_character_count(book_text)
		print(format_char_count(char_count))
		print("============= END ===============")
	except FileNotFoundError:
		print("Error: The file 'books/frankenstein.txt' was not found.")
  
if __name__ == "__main__":
	main()