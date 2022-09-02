# Communication Agent


Communication agent is the module that maintains the communication between the server and the android.

It spawns two threads, the first one is listening for messages on port 12345, and another one is used to send data to the android.

Two message queues are used for this purpose. The listener thread, reads a message and puts into a received_queue for the actual processing to be happened.

After the actual work is done, then the result (if there is any) is posted on the sending queue.

The sending thread looks into the sending queue, if there's a message to send, it sends the message.