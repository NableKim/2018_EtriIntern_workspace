try:
    import Image
except ImportError:
    from PIL import Image
from pytesseract import *

print(pytesseract.image_to_string(Image.open('googleAddress.jpg')))
