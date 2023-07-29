from pdf_preview import *

try:
    dpi_value = int(input("Input resolution in dpi: "))

    pdf_preview(dpi_value)
except ValueError:
    print("Wrong input, close...")

# input("Enter to close program.") # if needed