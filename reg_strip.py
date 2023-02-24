import re

# text = "  fu dge  "
#
# print(bool(re.search(r'\A | \Z', text)))
# print(re.findall(r'\A +| +\Z', text))
# print(re.sub(r'\A +| +\Z', "", text))


def remove_spaces(string, removed=" "):
    return print(re.sub(rf'\A{removed}+|{removed}+\Z', "", string))


remove_spaces("test", "t")
