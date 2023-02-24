#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, logging

import pyperclip

# Checks to see if the number of arguments passed to the command line is more than one. sys.argv is a list of strings,
# and sys.argv[0] is the filepath of the script.

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.debug(f"Contents of command line: {sys.argv}")
if len(sys.argv) > 1:
    # Get address from command line.
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
