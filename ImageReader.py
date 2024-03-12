import os
from tesserocr import get_languages
from tesserocr import PyTessBaseAPI
from PIL import Image

def list_image_files(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter files to include only images (adjust file extensions as needed)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    return image_files


def ocr_image(image_path):
    with PyTessBaseAPI() as api:
        api.SetImageFile(image_path)
        print(api.AllWordConfidences())
        text = api.GetUTF8Text()
        return text




images = list_image_files("Receipts/")
for img in images:
    img_path= "Receipts/"+img
    try:
        result_text = ocr_image(img_path)
        print("OCR Result:")
        print(result_text)
    except Exception as e:
        print(f"Error processing image: {e}")



"""
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

pdf_text = read_pdf('Recipts_as_PDF/TestPDFfile.pdf')
print(pdf_text)
"""