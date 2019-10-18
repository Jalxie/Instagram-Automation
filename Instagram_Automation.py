
import sys
import time
import logging
from instapy_cli import client

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEvent

from changeFileName import ModifyFilename


"""Instagram Auto Post"""
# username = 'jalxiey_'
# password = ''
# image = 'posts/post1.png'
# text = 'Upload from python'

# with client(username, password) as cli:
#     cli.upload(image, text)

"""File Monitor"""
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = '/Users/jalxiey/Documents/Coding/Github/Instagram-Automation/posts'
#     event_handler = LoggingEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#             print(event_handler)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

ModifyFilename()