import config
import picamera
import time


camera = picamera.PiCamera()


def filename(directory, extension):
    return "%s/%s.%s" % (directory, time.strftime("%Y-%m-%d_%H.%M.%S"), extension)


def take_picture():
    camera.capture(filename(config.photos_dir, "jpg"), )


def take_sequence(number=3):
    camera.capture_sequence([
        filename(config.photos_dir, "%02d.jpg") % i
        for i in range(number)
    ])


def record_video():
    camera.start_recording()
