import os
from PIL import Image
import pytesseract
from tqdm import tqdm


input_folder = "pdf_images"
output_file = "extracted_text.txt"

image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

image_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

with open(output_file, 'w', encoding='utf-8') as outfile:
    for image_file in tqdm(image_files, desc="Processing images"):
        image_path = os.path.join(input_folder, image_file)
        
        img = Image.open(image_path)
        
        text = pytesseract.image_to_string(img, lang='chi_tra+eng') 
        
        image_name = os.path.splitext(image_file)[0]

        outfile.write(f"--- {image_name} ---\n")
        outfile.write(text + '\n\n')

print(f"Down {output_file}")
