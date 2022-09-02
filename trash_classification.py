class TrashClassify:
    def __init__(self):
        self.request_number = 1

    def classify_trash(self, img):
        self.request_number += 1
        if self.request_number % 50 == 0:
            if self.request_number % 3 == 0:
                return 1
            elif self.request_number % 7 == 0:
                return 2
            elif self.request_number % 11 == 0:
                return 3 
        else:
            return 0        # No trash