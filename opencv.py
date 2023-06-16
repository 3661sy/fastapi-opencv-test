import cv2
import io


cam_obj = cv2.VideoCapture(0)


def get_camera():
    while True:
        ret_val, mat = cam_obj.read()
        if not ret_val:
            break

        ret_val, img = cv2.imencode('.jpg', mat)

        jpg_bin = bytearray(img.tobytes())

        yield (b'--PNPframe\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpg_bin + b'\r\n')


def get_camera_image():
    ret_val, mat = cam_obj.read()
    if ret_val:
        is_success, buffer = cv2.imencode('.jpg', mat)
        io_buf = io.BytesIO(buffer)
        return io_buf

