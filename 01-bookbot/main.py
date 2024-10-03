def open_book(name):
  with open(f'books/{name}.txt') as f:
      text = f.read()
  return text

def word_count(text):
  count = text.split()
  return len(count)

def char_count(text):
  chars = {}
  for char in text:
    lowered = char.lower()
    if lowered not in chars:
      chars[lowered] = 1
    else:
      chars[lowered] += 1

  return chars

def convert_and_sort(dict):
  char_lst = []

  def sort_key(inp):
    return inp['count']

  for item in dict:
    if item.isalpha():
      char_lst.append({'char': item, 'count': dict[item]})

  char_lst.sort(reverse=True, key=sort_key)

  return char_lst

def print_res(book_title, count, sorted):
  print(f'--- Begin report of books/{book_title}.txt ---')
  print(f'{count} words found in the document\n')

  for item in sorted:
    print(f"The '{item['char']}' character was found {item['count']} times")

  print('--- End report ---')

def main():
  book_title = 'frankenstein'
  text = open_book(book_title)
  count = word_count(text)
  chars = char_count(text)
  sorted = convert_and_sort(chars)
  print_res(book_title, count, sorted)

main()