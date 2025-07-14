# import krna para module jasko kaam cha docx lai pdf banaune
from docx2pdf import convert
import os  # yo module le file check garna madat garcha

# input file ko path (j hunu parcha docx format ma)
input_Path = "new.docx"

# output file ko path (yo banne wala ho pdf)
output_path = "new.pdf"

try:
    # sabse pahila check garum ki file xa ki nai
    if os.path.exists(input_Path):
        # aba convert garum docx file lai pdf ma
        convert(input_Path, output_path)
        print("✅ Successfully converted the DOCX into PDF.")
    else:
        # yedi file xaina vane yo message dekhauxa
        print("❌ File not found. Please check the filename or path.")
except Exception as e:
    # yedi kunai error ayo vane yo line execute hune
    print("❌ Something went wrong during conversion:", e)
