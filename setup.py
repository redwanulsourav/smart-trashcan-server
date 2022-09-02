import os

def main():
    if os.path.exists('face-dataset/') == False:
        os.mkdir('face-dataset')
        

if __name__ == '__main__':
    main()