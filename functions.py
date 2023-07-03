from PIL import Image
from pathlib import Path
import sys, os

IN_FOLDER = "in"
OUT_FOLDER = "out"

def _resize_image(imageFile, resize_value):
    pass

# Convert png images to jpeg
def png_to_jpeg(imageFile):
    try:
        with Image.open(imageFile) as img:
            # IF image already jpeg, do nothing
            if img.format == "JPEG":
                print("[!] Image is already Jpeg.")
            else:
                if img.mode != "RGB":
                    print("[!] Converting image to RGB mode.")
                    img = img.convert("RGB")
                    # From the image file/path, remove all other than the base file name
                    fileName = os.path.basename(imageFile)
                    # Construct the name for the image from the original filename and replace the extension with jpeg
                    img.save(os.path.join(OUT_FOLDER, os.path.splitext(fileName)[0] + ".jpeg"),"JPEG")
                    img.close()
    except OSError as e:
        print(f"[-] Error opening the image..")
        print(e)

# Do tests here
def _test():
    img = "in/blue_dreams.png"
    png_to_jpeg(img)
