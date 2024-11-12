'''Analyses contents of .txt files'''
from collections import Counter
import string

file_path = 'books/frankenstein.txt'

def get_file_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    return len(text.split())


def char_count(text):
    # Convert text to lowercase and count character occurrences
    counter = Counter(text.lower())
    
    # Separate letters and other characters, sorted alphabetically within each group
    letters = {k: counter[k] for k in sorted(counter) if k in string.ascii_lowercase}
    others = {k: counter[k] for k in sorted(counter) if k not in string.ascii_lowercase}
    
    # Format each group into strings with new lines
    formatted_letters = "\n".join(f"{char}: {count}" for char, count in letters.items())
    formatted_others = "\n".join(f"{char}: {count}" for char, count in others.items())
    
    # Combine both groups, with letters first
    return f"{formatted_letters}\n{formatted_others}"


contents  = get_file_contents(file_path)
print(f"\n------------ Report: {file_path} ------------")
print(f"Number of words: {count_words(contents)}")
print(f"\n\nCharacter analysis:\n\n{char_count(contents)}")
print("\n\n ------------ END ------------")