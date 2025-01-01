import pytesseract as pyt
import cv2

img = cv2.imread("expression.png")
text = pyt.image_to_string(img)

list1 = text.split()
a = int(list1[0])
b = int(list1[2])
if list1[1] == '+':
  print(a+b)
elif list1[1] == '-':
  print(a-b)
elif list1[1] == '*':
  print(a*b)
elif list1[1] == '/':
  print(a/b)
