#!/usr/bin/python3
# -*- coding: utf-8 -*-
import face_recognition
import cv2
import random
import freenect
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.


# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [

]
known_face_names = [

]

# List of all undergraduate degrees on the Federal University of Parana
cursos = {
"Administracao ": (0, 0, 179),
"Agronomia ": (36, 143, 36),
"Arquitetura e Urbanismo ": (0, 0, 179),
"Artes Visuais ": (0, 0, 179),
"Biomedicina ": (255, 209, 26),
"Ciencias Biologicas ": (255, 209, 26),
"Ciencia da Computacao ": (204, 0, 0),
"Ciencias Contabeis ": (0, 0, 179),
"Ciencias Economicas ": (0, 0, 179),
"Ciencias Sociais ": (0, 0, 179),
"Design Grafico ": (153, 0, 153),
"Design de Produto ": (153, 0, 153),
"Direito ": (153, 0, 153),
"Educacao Fisica ": (0, 0, 179),
"Enfermagem ": (0, 0, 179),
"Eng. Ambiental ": (36, 143, 36),
"Eng. de Bioprocessos ": (36, 143, 36),
"Eng. Cartografica ": (0, 0, 179),
"Eng. Civil ": (204, 0, 0),
"Eng. Eletrica ": (204, 0, 0),
"Eng. Florestal ": (36, 143, 36),
"Eng. Indust. Madeireira ": (36, 143, 36),
"Eng. Mecanica ": (204, 0, 0),
"Eng. de Producao ": (204, 0, 0),
"Eng. Quimica ": (204, 0, 0),
"Estatistica ": (204, 0, 0),
"Expressao Grafica ": (153, 0, 153),
"Informatica Biomedica ": (255, 209, 26),
"Farmacia ": (36, 143, 36),
"Filosofia ": (0, 0, 179),
"Fisica ": (204, 0, 0),
"Fisioterapia ": (0, 0, 179),
"Geografia ": (0, 0, 179),
"Geologia ": (0, 0, 179),
"Gestao da Informacao ": (0, 0, 179),
"Historia ": (0, 0, 179),
"Jornalismo ": (0, 0, 179),
"Letras ": (0, 0, 179),
"Letras Libras ": (0, 0, 179),
"Matematica ": (204, 0, 0),
"Matematica Industrial ": (204, 0, 0),
"Medicina ": (153, 0, 153),
"Med. Veterinaria ": (153, 0, 153),
"Musica ": (153, 0, 153),
"Nutricao ": (153, 0, 153),
"Odontologia ": (153, 0, 153),
"Pedagogia ": (0, 0, 179),
"Psicologia ": (153, 0, 153),
"Publicidade e Propaganda ": (153, 0, 153),
"Quimica ": (204, 0, 0),
"Relacoes Publicas ": (0, 0, 179),
"Tec. Desenv. de Sistemas ": (0, 0, 179),
"Tec. Com. Institucional ": (0, 0, 179),
"Tec. Gestao Publica ": (0, 0, 179),
"Tec. Gestao da Qualidade ": (0, 0, 179),
"Tec. Luteria ": (0, 0, 179),
"Tec. Negocios Imobiliarios ": (0, 0, 179),
"Tec. Producao Cenica ": (0, 0, 179),
"Tec. Secretariado ": (0, 0, 179),
"Terapia Ocupacional ": (0, 0, 179),
"Turismo ": (153, 0, 153),
"Zootecnia ": (36, 143, 36),
}

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

RESIZE = 0.25
SCALE_MULT = int(float(1)/RESIZE)

while True:
    
    # Grab a single frame of video
    image,_ = freenect.sync_get_video()
    frame = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=RESIZE, fy=RESIZE)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame,number_of_times_to_upsample=2, model='hog')
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
   
            scores = face_recognition.face_distance(known_face_encodings, face_encoding)
            
            name = ""
            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                maiorScore = 0
                for i,x in enumerate(scores):
                    if(scores[i] > scores[maiorScore]):
                        maiorScore = i
                
                first_match_index = maiorScore
                name = known_face_names[first_match_index]
            else:
                random_course = random.choice(list(cursos))
                name = random_course
                known_face_names.append(name)
                known_face_encodings.append(face_encoding)
            
            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size

        top *= SCALE_MULT
        right *= SCALE_MULT
        bottom *= SCALE_MULT
        left *= SCALE_MULT

        # Draw a box around the face
        cv2.rectangle(frame, (left - 27, top - 35), (right + 27, bottom), (204, 204, 0), 1)
        
        # Draw a label with a name below the face
        current_h, pad = 0, 0
        cv2.rectangle(frame, (left - 25, bottom + 40), (right + 25, bottom), cursos[name], cv2.FILLED)
        para = []
        index_string_break = 1
        text_width = 0
        # breaks line to fit on the rectangle
        while((text_width < right-left+54) and (index_string_break < len(name))):
            text_width = cv2.getTextSize(name[:index_string_break], cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 1)[0][0]
            index_string_break+=1

        index_string_break-=1
        
        para = [
            name[:index_string_break],
            name[index_string_break:]
        ]

        for line in para:
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            font_scale = 0.9
            margin = 5
            thickness = 2
            color = (255, 255, 255)


            size = cv2.getTextSize(line, font, font_scale, thickness)
            text_height = size[0][1]
            h = text_height + size[1] + margin
            cv2.putText(frame, str(line), (left - 18, bottom + 20 + current_h), font, font_scale, (255, 255, 255), 1)
            current_h += 14 + pad
        

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
# video_capture.release()
cv2.destroyAllWindows()
