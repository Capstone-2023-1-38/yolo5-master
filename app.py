import numpy as np
from flask import Flask, render_template, Response
from multiprocessing import shared_memory
import time
import cv2
import torch
# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse

app = Flask(__name__)

# model = torch.hub.load(r"/", 'custom', path=r"D:\졸업과제\yolov5-master\yolov5s.pt", source='local', force_reload=True, autoshape = True)

# cap = cv2.VideoCapture(0)
@app.route('/')
def video_show():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return render_template('video_show.html')

# @app.before_request
# def getFrame():
    # if request.method == "POST":
    #     nparr = np.frombuffer(frame, np.uint8)
    #     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #     # framedata = (b'--frame\r\n'
    #     #            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    # return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():
    while True:
        time.sleep(0.01)
        frame_shm = shared_memory.ShareableList(name="frame")
        yield (b'--frame\r\n'
                      b'Content-Type: image/jpeg\r\n\r\n' + frame_shm[1][:frame_shm[0]] + b'\r\n')

        # _, frame = cap.read()
        # if not _:
        #     break
        # else:
        #     # results = model(frame)
        #     # annotated_frame = results.render()
        #
        #     ret, buffer = cv2.imencode('.jpg', frame)
        #     frame = buffer.tobytes()
        #
        # yield (b'--frame\r\n'
        #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
