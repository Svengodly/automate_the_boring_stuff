# Practice opening files

filepath = '/Users/rmorr/Desktop/reviewCisco.txt'

with open(filepath) as file_object:
    content = file_object.read()
print(content)

print(__name__)