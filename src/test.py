import pytesseract
import cv2
from difflib import SequenceMatcher as SQ

config = ('-l kor+eng --oem 3 --psm 6')

img_path = '/app/data/validation/data1.tif'
txt_path = '/app/data/validation/data1.txt'

f = open(txt_path, 'r')
target = f.read()
f.close()

img = cv2.imread(img_path)
raw_text = pytesseract.image_to_string(img, config=config) 
print(f"Output:\n{raw_text}\n\nPercent coincidence:{round(SQ(None, target, raw_text).ratio()*100,2)}%")
