# importing Converter class from pdf2docx module
from pdf2docx import Converter

# define the file names
old_pdf = "Profile.pdf"  # this is the input PDF file
new_pdf = "new.docx"     # this will be the output DOCX file

try:
    # create the converter object
    obj = Converter(old_pdf)

    # convert the PDF to DOCX
    obj.convert(new_pdf)

    # close the converter
    obj.close()

    print("✅ Successfully converted the PDF file into a DOCX file.")
except Exception as e:
    print("❌ Oops! Something went wrong:", e)