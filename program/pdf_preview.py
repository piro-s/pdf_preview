import os

# install pdf2jpg library (pip install pdf2jpg) # https://github.com/pankajr141/pdf2jpg
from pdf2jpg import pdf2jpg


def pdf_preview(dpi_value=50):
    directory = os.getcwd() # assign directory

    # process all pdf in directory
    for filename in os.listdir(directory):
        pdf = os.path.join(directory, filename)
        if os.path.isfile(pdf) and pdf.split('.')[-1].lower() == 'pdf': # if it's file and pdf
            inputpath = pdf
            outputpath = r""
            result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=dpi_value, pages="ALL")


if __name__ == '__main__':
    pdf_preview()