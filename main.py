from stats import count_words, chars_in_text

def get_book_text(filepath: str):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  contents = get_book_text("./books/frankenstein.txt")
  word_count = count_words(contents)
  print(f'Found {word_count} total words')
  print(chars_in_text(contents))

main()
