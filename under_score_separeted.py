import re
import pyperclip

def process_text(text):
    text = text.lower()
    words = re.split(' |-', text)
    return '_'.join(words)


inp = input('Enter text: ')
print(process_text(inp))