def count_words(text: str):
  words = text.split()
  return len(words)

def chars_in_text(text: str):
  chars = {}
  lower_text = text.lower()
  for i in range(len(lower_text)):
    if lower_text[i] not in chars:
      chars[lower_text[i]] = 1
    else:
      chars[lower_text[i]] += 1
  return chars
