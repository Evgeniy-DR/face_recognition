from fileinput import filename
from pathlib import Path
import os
from tkinter.scrolledtext import example
import face_recognition
from PIL import Image, ImageDraw


BASE_DIR = Path(__file__).resolve().parent
image_path = os.path.join(BASE_DIR, 'example.jpg')


image = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(image)

# find and outpue face image_______________________________________
# for face_location in face_locations:
#     top, right, botton, left = face_location
#     print("Our four photo 1: {}, 2: {}, 3: {}, 4: {},".format(top, right, botton, left))
#     face_image = image[top:botton, left:right]
#     print_image = Image.fromarray(face_image)
#     print_image.show()
    
# print('I finde {} face(s) in photo'.format(len(face_location)))
# print('path: ___', image_path)
# print('path BASE_DIR: ___', BASE_DIR)
# ________________________________________________________________

face_landmarks_list = face_recognition.face_landmarks(image)
pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(pil_image)


for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
    
    for facial_feature in face_landmarks.keys():
        draw.line(face_landmarks[facial_feature], width=10)




pil_image.show()
