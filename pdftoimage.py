from pdf2image import convert_from_path
import os

pdf_path = "/home/user/workspace/ocr/PerspectivesOnLearning.pdf"

output_folder = "pdf_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

images = convert_from_path(pdf_path)

for i, image in enumerate(images):
    image.save(f"{output_folder}/page_{i+1}.png", "PNG")

print(f"Save in  {output_folder} ")
