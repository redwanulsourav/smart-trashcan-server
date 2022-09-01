import face_recognition

class Dataset:
    def __init__(self):
        self.face_encodings = []
        self.face_names = []

        self.face_count = 0

        # Load dataset.

        face_dirs = os.listdir('face-dataset/')

        for single_face in face_dirs:
            img_path = f'face-dataset/{single_face}/0.jpg'
            face_name = f'face-dataset/{single_face}/name.txt'

            # Extract name
            f = open(face_name, 'r')
            contents = f.read()
            f.close()

            # Clean up the contents.
            name = contents.strip()

            img = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(img)[0]

            self.face_encodings.append(encoding)
            self.face_names.append(name)

    
    def known_face_encodings(self):
        return self.face_encodings()
    
    def get_face_name_idx(self, idx):
        if idx < len(face_names) and idx >= 0:
            return self.face_name[idx]
        

    