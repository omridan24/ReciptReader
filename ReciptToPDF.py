from PIL import Image
from reportlab.pdfgen import canvas
import os
"""
def convert_image_to_pdf(image_path, output_pdf):
    try:
        # Open the image and get its dimensions
        img = Image.open(image_path)
        width, height = img.size

        # Create a new PDF file
        with open(output_pdf, 'wb') as pdf_file:
            pdf = canvas.Canvas(pdf_file)

            # Set the page size based on the image dimensions
            pdf.setPageSize((width, height))

            # Add the image to the PDF
            pdf.drawImage(image_path, 0, 0, width, height)

            # Save the PDF file
            pdf.save()

        print(f"Successfully converted {image_path} to {output_pdf}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

    


input_folder_path = "Recipts"
output_folder_path = "Recipts_as_PDF"
os.makedirs(output_folder_path, exist_ok=True)
# List all files in the input folder
files = os.listdir(input_folder_path)

# Iterate through each file in the folder
for file_name in files:
    # Construct the full path to the image file
    image_path = os.path.join(input_folder_path, file_name)

    # Check if the item is a file and ends with a common image extension
    if os.path.isfile(image_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Construct the output PDF path
        output_pdf_path = os.path.join(output_folder_path, os.path.splitext(file_name)[0] + ".pdf")

        # Convert the image to a PDF
        convert_image_to_pdf(image_path, output_pdf_path)

"""
print("hello")