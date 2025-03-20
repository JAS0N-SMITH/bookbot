def get_book_text(path) -> str:
	"""Reads the content of a book from a file and returns it as a string."""
	with open(path, 'r', encoding='utf-8') as file:
		return file.read()

def get_number_of_words(text: str) -> int:
	"""Counts the number of words in a given text."""
	print("----------- Word Count ----------")
	return len(text.split())

def get_character_count(text: str) -> dict:
	"""Counts the occurrences of each character in the text."""
	char_count = {}
	for char in text.lower():
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def format_char_count(char_count: dict) -> str:
	"""takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary should have two key-value pairs: one for the character and one for the count.
    Sort from greatest to least by the count.
    The .sort() method will be helpful here (see the hint).
	"""
	print("--------- Character Count ----------")
	# Create a list of dictionaries, each containing the character and its count. If the character is not an alphabetical character (using the .isalpha() method), just skip it.
	char_count_list = [{'character': char, 'count': count} for char, count in char_count.items() if char.isalpha()]
	# Sort the list from greatest to least by the count.
	char_count_list.sort(key=lambda x: x['count'], reverse=True)
	# format the result as a string with each character and its count on a new line.
	formatted_result = "\n".join(f"{item['character']}: {item['count']}" for item in char_count_list)
	# return the formatted string.
	return formatted_result
