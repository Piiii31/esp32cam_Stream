# In views.py
from django.http import StreamingHttpResponse
import urllib.request
import threading
import queue
from rest_framework.decorators import api_view
import cv2
import numpy as np

# Replace the URL with the IP camera's stream URL
url = 'https://lightly-huge-mantis.ngrok-free.app/cam-lo.jpg'

# Create a queue to hold the frames
frame_queue = queue.Queue()

def read_frames():
    # This function will run in a separate thread
    while True:
        # Read a frame from the video stream
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)

        # Put the frame in the queue
        frame_queue.put(im)

# Start the read_frames function in a separate thread
threading.Thread(target=read_frames).start()

def gen():
    # Generator function to stream video frames
    while True:
        # Get a frame from the queue
        im = frame_queue.get()

        _, jpeg = cv2.imencode('.jpg', im)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@api_view(['GET'])
def videofeed(request):
    # View function to serve the video feed
    return StreamingHttpResponse(gen(), content_type='multipart/x-mixed-replace; boundary=frame')