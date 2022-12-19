from fileinput import filename
from pathlib import Path
import os
from tkinter.scrolledtext import example
import face_recognition
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent.parent
image_path = os.path.join(BASE_DIR, 'example.jpg')


image = face_recognition.load_image_file('example.jpg')
face_locations = face_recognition.face_locations(image)
for face_location in face_locations:
    top, right, botton, left = face_location
    face_image = image[top:botton, left:right]
    print_image = Image.fromarray(face_image)
    print_image.show()
    

    # print('I finde {} face(s) in photo'.format(len(face_location)))
    # print('path: ___', image_path)


