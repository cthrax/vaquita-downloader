"""
This module represents the connection to the camera
"""

import csv
import ftplib
import logging
import pathlib

import camera_instance

from vaquita_downloader.directory_listing import DirectoryListing

CAMERA_LOG_DIR = '/var/www/DCIM/LOGS'


class Buffer:
    """
    This class allows the addition of in-memory data without modifying the reference
    """
    def __init__(self):
        self.buffer = b''

    def add_chunk(self, chunk: bytes):
        """
        Appends to instance buffer
        :param chunk: the bytes to be added to buffer
        :return: None
        """
        self.buffer += chunk


class CameraSession:
    """
    A camera session is basically an FTP session to the device.
    This holds the state of the FTP session plus some static variables.
    As well as wrapping up some functionality that is maybe multiple steps.
    """
    host = '192.168.42.1'
    username = 'vaquita'
    password = 'vaquita'

    def __init__(self, cache_dir=None, verbosity=logging.INFO):
        if cache_dir is None:
            self.cache_dir = './logs'
        self.verbosity = verbosity

        self.cache_dir_path = pathlib.Path(self.cache_dir)
        self.cache_dir_path.mkdir(parents=True, exist_ok=True)

        self.server = None
        self.camera = None

    def initiate_session(self):
        self.server = self.connect_to_server()
        self.camera = self.retr_camera_info(self.server)

    def import_new_media(self):
        for path in self.cache_dir_path.glob("*.csv"):
            with open(path.absolute(), 'r') as f:
                csv_reader = csv.DictReader(f)
                for line in csv_reader:
                    # There is a filename to the image or video and if a video,
                    # there may be multiple timestamps for the video depending on the duration
                    # of the video.
                    # TODO:
                    #   1. Get a list of files that need to be transferred
                    #   2. Determine what log files have already been processed (thinking putting .done on end of name)
                    #   3. Try to get last GPS coordinates from a log
                    #   4. Fix date/time of videos based on log datetime
                    #   5. Maybe do something fun with the dive log/depth/temperature
                    #   6. Maybe import into subsurface
                    #   7. Maybe add feature to subsurface to link media files in connected or disconnected state
                    time = line['Time']
    def download_new_logs(self):
        if not self.is_connected():
            self.initiate_session()

        server = self.connect_to_server()
        camera = self.retr_camera_info(server)
        listing = self.get_log_listing(server)
        self.download_unknown_logs(server, listing)

    def is_connected(self):
        return self.server is not None

    def download_unknown_logs(self, server: ftplib.FTP, listing: DirectoryListing):
        for filename in listing.filenames:
            path = pathlib.Path(self.cache_dir, filename)
            if not path.exists():
                with open(path.absolute(), 'wb') as f:
                    server.retrbinary(f'RETR {filename}', f.write)

    def get_log_listing(self, server: ftplib.FTP):
        server.cwd(f'{CAMERA_LOG_DIR}')

        dir_listing = DirectoryListing()
        server.dir(lambda chunk, dir_listing=dir_listing: dir_listing.add_bytes(chunk))
        dir_listing.assemble()
        return dir_listing

    def retr_camera_info(self, server: ftplib.FTP):
        buffer = Buffer()

        def retr_callback(block, buffer=buffer):
            buffer.add_chunk(block)

        server.retrbinary(f'RETR {camera_instance.INFO_FILE_NAME}', retr_callback)
        camera = camera_instance.Camera(buffer.buffer)
        response = server.sendcmd(f'MDTM {camera_instance.INFO_FILE_NAME}')
        camera.set_modified(response)
        return camera

    def connect_to_server(self):
        server = ftplib.FTP(self.host, self.username, self.password)
        server.debug(self.verbosity)
        server.login(self.username, self.password)
        server.sendcmd('TYPE I')
        server.sendcmd('SYST')
        server.sendcmd('FEAT')
        server.sendcmd('OPTS UTF8 ON')
        server.set_pasv(True)

        return server
