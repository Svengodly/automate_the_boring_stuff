import os

filepath = "E:/INFO 474"

with os.scandir(filepath) as folder:
    for item in folder:
        size = item.stat()
        print(item.name, (size.st_size / 1024))


