import queue
import threading
import socket
import greeting_helper
import os
import json
from threading import Lock
import PIL.Image
from io import BytesIO
import base64
import cv2
import numpy as np


received_messages = queue.Queue()
sending_messages = queue.Queue()

greeting_agent = greeting_helper.GreetingHelper()

def server_send():
    s = socket.socket()
    port = 12346
    s.connect(('127.0.0.1', port))

    while True:
        # print("Sending")
        if sending_messages.qsize() > 0:
            message = sending_messages.get()
            
            lock = Lock()
            lock.acquire()
            print(message)
            lock.release()
            
            s.send(message.encode('utf-8'))

def server_receive():
    global received_messages

    s = socket.socket()
    port = 12345
    
    s.bind(('', port))
    s.listen()
    incoming_data = ''
    c, addr = s.accept()
    # x = threading.Thread(target = serve_send)
    # x.start()
    print('Got connection from', addr)
    total_data = ''
    while True:  
        try:  
            incoming_part_data = c.recv(204800).decode();
            print('incoming_part_data:', incoming_part_data)
            
            idx = incoming_part_data.find('$')

            if idx != -1:
                total_data = total_data + incoming_part_data[:idx+1]
                
                assert total_data[-1] == '$', 'Data should end with $'
                assert total_data[0] == '^', 'Data should start with ^'
                
                total_data = total_data[1:-1]
                print(total_data)
                json_data = json.loads(total_data)
                
                received_messages.put(json_data)

                total_data = incoming_data[idx + 1: ]
                """
                imgdata = base64.b64decode(json_data["data"])
                jpg_as_np = np.frombuffer(imgdata, dtype=np.uint8)
                img = cv2.imdecode(jpg_as_np, flags=1)
                dim = (640, 480)
                img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                
                name = face_recog(img)
                print('name: ', name)
                #cv2.imshow('img',img)
                #cv2.waitKey(1)
                
                message_dict = {
                    'name' : name
                }
                message_queue.put('^' + json.dumps(message_dict) + '$')
                # print(message_queue.qsize())
                total_data = incoming_part_data[idx + 1: ]
                """
            else:
                total_data = total_data + incoming_part_data
        except:
            s.close()
            break    
    
        # print(len(incoming_part_data))
        # json_file = json.loads(incoming_data)
        # image = json_file['data']
        # name = json_file['name']
        # im = PIL.Image.open(BytesIO(base64.b64decode(image)))
        # frame, pname = face(im)
        # serve_send(frame, pname)
        # c.close()
        # s.close()

    # cv2.destroyAllWindows()


def process():
    global received_messages
    global sending_messages
    global greeting_agent

    lock = Lock()
    lock.acquire()
    print("process started")
    lock.release()

    while True:
        
        if received_messages.qsize() > 0:
            message = received_messages.get()

            lock = Lock()
            lock.acquire()
            print("message:",message)
            lock.release()
                

            if message["type"] == 'FACE_RECOG_SERVICE':
                # Recover the image from base64 encoding.

                imgdata = base64.b64decode(message["data"])
                jpg_as_np = np.frombuffer(imgdata, dtype=np.uint8)
                img = cv2.imdecode(jpg_as_np, flags=1)

                # img = PIL.Image.open(BytesIO(base64.b64decode(message["data"])))

                name = greeting_agent.face_recognition(img)
                
                # Have to send name here.
                lock = Lock()
                lock.acquire()
                print("name:",name)
                lock.release()
                
                response_message = {
                    'type' : 'FACE_RECOGNITION_RESPONSE',
                    'name' : name
                }

                response_message_str = '^' + json.dumps(response_message) + '$'
                sending_messages.put(response_message_str)



if __name__ == '__main__':
    
    receiving_thread = threading.Thread(target = server_receive)
    receiving_thread.start()

    sending_thread = threading.Thread(target = server_send)
    sending_thread.start()

    process_thread = threading.Thread(target = process)
    process_thread.start()
    
    while True:
        pass
        