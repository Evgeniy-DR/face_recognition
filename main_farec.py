from fileinput import filename
from pathlib import Path
import os
from tkinter.scrolledtext import example
import face_recognition
from PIL import Image, ImageDraw

BASE_DIR = Path(__file__).resolve().parent
image_path_original = os.path.join(BASE_DIR, 'picture example/example.jpg')
image_path_to_compare = os.path.join(BASE_DIR, 'picture example/example_to_compare_false.jpg')


def compare_images(original, compare):
    image_first = face_recognition.load_image_file(original)
    image_first_encoding = face_recognition.face_encodings(image_first)[0]

    image_second = face_recognition.load_image_file(compare)
    image_second_encoding = face_recognition.face_encodings(image_second)[0]

    compare_face = face_recognition.compare_faces([image_first_encoding], image_second_encoding)
    # print(compare)
    if compare_face[0] == True:

        face_locations = face_recognition.face_locations(image_first)
        # find and output face image_______________________________________
        for face_location in face_locations:
            top, right, bottom, left = face_location
            print("Our four photo 1: {}, 2: {}, 3: {}, 4: {},".format(top, right, bottom, left))
            face_image = image_first[top:bottom, left:right]
            print_image = Image.fromarray(face_image)
            return print_image.show()
    else:
        print('This face is not from our base')
        # print('I finde {} face(s) in photo'.format(len(face_location)))
        # print('path: ___', image_path_to_compare)
        # print('path BASE_DIR: ___', BASE_DIR)
        # ________________________________________________________________



# ______use compare function______
compare_images(image_path_original, image_path_to_compare)












#_________________________________________check face and draw the line_
# face_landmarks_list = face_recognition.face_landmarks(image)
# pil_image = Image.fromarray(image)
# draw = ImageDraw.Draw(pil_image)
#
# for face_landmarks in face_landmarks_list:
#     for facial_feature in face_landmarks.keys():
#         print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
#
#     for facial_feature in face_landmarks.keys():
#         draw.line(face_landmarks[facial_feature], width=4)
#
# pil_image.show()
