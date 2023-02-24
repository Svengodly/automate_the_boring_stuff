import zipfile, os, re

# TO DO: Make it so that the only folder names that print are the ones that contain zip files

theWalk = os.walk("C:\\Users\\rmorr\\Downloads")

for foldername, subfolders, filenames in theWalk:
    for filename in filenames:
        if re.search("zip\\b", filename) is not None:
            print(filename)
    print(f"Folder: {foldername}")
    # print(f"Subfolder of {foldername}: {filename}")
    
