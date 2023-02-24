import re
import pyperclip

# Phone and Email regex.
phoneExp = re.compile(r'\d{3}[\s.]\d{3}[\s.]\d{4}')

emailExp = re.compile(r'\S+@[a-zA-Z]+[0-9]*\.[a-zA-Z]+[0-9]*')

# Use pyperclip's paste() method to capture text from the clipboard.
text = pyperclip.paste()

# Apply Regex to text
matches = []

for match in phoneExp.findall(text):
   # print(match[0])
    matches.append(match)

for match in emailExp.findall(text):
    matches.append(match)

if len(matches) > 0:
    # Copy matches to clipboard
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No matches found.")
