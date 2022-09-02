import db_interface
import face_recognition

class GreetingHelper:
    def __init__(self):
        self.face_database = db_interface.Dataset()
    
    def face_recognition(self, face_crop):
        """
            Parameters: face_crop - OpenCV BGR image.
            Returns: Name of recognized face or Unknown.
        """

        # Conver BGR to RGB
        face_crop = face_crop[:, :, ::-1]
        face_crop_encoding = face_recognition.face_encodings(face_crop)
        
        # If there are no faces, return None, will handle this case from the caller.
        if len(face_crop_encoding) == 0:
            return None

        face_crop_encoding = face_crop_encoding[0]

        name = 'Unknown'
        
        matches = face_recognition.compare_faces(self.face_database.known_face_encodings(), face_crop_encoding)
        
        if True in matches:
            first_match_index = matches.index(True)
            name = self.face_database.get_face_name_idx(first_match_index)
        
        return name
    

if __name__ == '__main__':
    #faceRecogIf = FaceRecogIf()p
    gh = GreetingHelper()