import os
import threading
import time
import asyncio

import subprocess

import config
import photography as cam


class UploadThread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.active = True

    def run(self):
        while self.active:
            upload_media()
            time.sleep(config.seconds_between_upload_retries)

    def stop(self):
        self.active = False


def take_picture():
    print("Taking picture")
    cam.take_picture()
    time.sleep(config.seconds_between_photos)


def upload_media():
    photos = [f for f in os.listdir(config.photos_dir) if os.path.isfile(os.path.join(config.photos_dir, f))]
    for photo in photos[:-1]:
        # don't upload latest photo, it might still be writing.

        print("Uploading %s" % photo)
        subprocess.call(['rclone', 'move', os.path.join(config.photos_dir, photo), config.cloud_photos_dir])

    print("Uploading videos")
    videos = [f for f in os.listdir(config.videos_dir) if os.path.isfile(os.path.join(config.videos_dir, f))]
    for video in videos[:-1]:
        # don't upload latest video, it might still be writing.

        print("Uploading %s" % video)
        subprocess.call(['rclone', 'move', os.path.join(config.videos_dir, video), config.cloud_videos_dir])


def prepare_directories():
    print("Making sure directories exist.")
    os.makedirs(config.data_dir, exist_ok=True)
    os.makedirs(config.photos_dir, exist_ok=True)
    os.makedirs(config.videos_dir, exist_ok=True)


def main():
    print("Starting")

    prepare_directories()
    upload_thread = UploadThread()
    upload_thread.start()

    try:
        while True:
            take_picture()
            time.sleep(config.seconds_between_photos)

    except KeyboardInterrupt:
        upload_thread.stop()


if __name__ == "__main__":
    main()
