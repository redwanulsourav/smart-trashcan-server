# Greeting Service


This module performs the task of face recognition for the greeting purpose. 

The module should implement following interfaces.


## Interfaces

`save_face(img, name): None`

**Parameters:**

*img*: An BGR OpenCV image which is a cropped face of a person. 
*name*: The name for the corresponding face.

**Returns**: *None*

`recognize_face(img): string`

**Parameters:**

*img*: An BGR OpenCV image which is a cropped face of a person.

**Returns**: The name of the person or *Unknown* if the person is unknown.



## Implementation Details

We will maintain the face database as a directory with face images and names. 

Each directory will contain one image, named specifically as `face.jpg` and a text file containing a name `name.txt`. 

### The sample directory structure

    |
    |-- 0
    |   |
    |   |-- face.jpg
    |   |-- name.txt
    |
    |-- 1
    |   |
    |   |-- face.jpg
    |   |-- name.txt


For face recognition task, we will use the python library found at [here](https://github.com/ageitgey/face_recognition). Some examples of using this library can be found [here](https://github.com/ageitgey/face_recognition/tree/master/examples).

