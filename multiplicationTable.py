import openpyxl
from openpyxl.styles import Font


"""Generates a multiplication table of X by X dimensions from user input."""
# flag = False
# while not flag:
#     try:
#         dimension = int(input("Please enter the dimension of the table: "))
#         if dimension < 1:
#             print("Must be an integer greater than 0.")
#             continue
#         else:
#             print(f"Creating a {dimension}x{dimension} table...")
#             flag = True
#     except ValueError:
#         print("Invalid input.")

mulTableWorkBook = openpyxl.Workbook()

mulTableSheet = mulTableWorkBook.active

mulTableSheet.title = "Multiply"

rowHeaders = mulTableSheet["A2:A6"]
columnHeaders = mulTableSheet["B1:F1"]

# columnHeaders consists of a single tuple within another tuple: Each cell is in the same tuple. I can access each
# element by passing an index.
for number in range(5):
    for cell in columnHeaders:
        cell[number].value = number + 1
        print(cell[number], cell[number].value)

# rowHeaders consists of tuples within a tuple: Each cell is in its own tuple. The for loop returns a tuple, containing
# just one cell object.
for cell in rowHeaders:
    cell[0].value = cell[0].row - 1
    print(cell[0], cell[0].value)

# Select area of workbook that will contain the products of the numbers
productRange = mulTableSheet["B2:F6"]

# Iterates over each tuple, which is a row of cell objects. The numbers to be multiplied can be retrieved by the
# numerical value of the rows and columns subtracted by 1.
for group in productRange:
    for number in range(len(group)):
        group[number].value = (group[number].row - 1) * (group[number].column - 1)
        print(group[number], group[number].value)

# Saves workbook in current working directory.
mulTableWorkBook.save('multiplicationTable.xlsx')
# print(productRange)