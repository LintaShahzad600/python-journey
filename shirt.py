import sys
from PIL import Image, ImageOps
valid_extensions = [".jpg", ".jpeg", ".png"]
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
input_file = sys.argv[1]
output_file = sys.argv[2]
if not input_file.lower().endswith(tuple(valid_extensions)):
    sys.exit("Invalid input")
if not output_file.lower().endswith(tuple(valid_extensions)):
    sys.exit("Invalid output")
if input_file.lower().split(".")[-1] != output_file.lower().split(".")[-1]:
    sys.exit("Input and output have different extensions")
try:
    shirt = Image.open("shirt.png")
    image = Image.open(input_file)
    size = shirt.size
    image = ImageOps.fit(image, size)
    image.paste(shirt, shirt)
    image.save(output_file)
except FileNotFoundError:
    sys.exit("Input does not exist")
