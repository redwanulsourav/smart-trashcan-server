import face_recognition
import os

class Dataset:
    def __init__(self):
        self.face_encodings = []
        self.face_names = []

        self.face_count = 0

        # Load dataset.

        face_dirs = os.listdir('face-dataset/')
        face_files = open('list.txt', 'r')
        faces = face_files.read()
        faces = faces.split(',')
        for single_face in face_dirs:
            img_path = f'face-dataset/{single_face}'
            #face_name = f'face-dataset/{single_face}/name.txt'

            # Extract name
            # f = open(face_name, 'r')
            # contents = f.read()
            # f.close()

            # Clean up the contents
            image_index = os.path.splitext(single_face)[0]
            image_index = int(image_index)
            name = faces[image_index].strip()

            img = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(img)[0]

            self.face_encodings.append(encoding)
            self.face_names.append(name)

    
    def known_face_encodings(self):
        return self.face_encodings
    
    def get_face_name_idx(self, idx):
        if idx < len(self.face_names) and idx >= 0:
            return self.face_names[idx]

    def refresh_db(self, img_path, name):
        img = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(img)[0]

        self.face_encodings.append(encoding)
        self.face_names.append(name)



    
