import datetime
import json

from vaquita_downloader.utils import UTC

INFO_FILE_NAME = '.camera.json'

class Camera:

    def __init__(self, json_bytes=None):
        self.parsed_time = None
        self.video_count = None
        self.photo_count = None
        self.temperature_unit = None
        self.depth_unit = None
        self.timezone = None
        self.time = None
        self.session_count = None
        self.id = None
        self.firmware = None

        if json_bytes is not None:
            string = str(json_bytes, 'utf-8')
            self.set_from_json(json.loads(str(json_bytes, 'utf-8')))


    def set_from_json(self, json_dict):
        """
        Camera Info Example
        {
            "firmware": "22.07.50954",
            "id": "704A0E2AA5DF",
            "session": 114,
            "time": 1672416745,
            "timezone": "UTC-04:00",
            "depth unit": "METER",
            "temperature unit": "CELSIUS",
            "photos": 635,
            "videos": 0
        }
        :param json_dict:
        :return:
        """
        self.firmware = json_dict['firmware']
        self.id = json_dict['id']
        self.session_count = json_dict['session']
        self.time = json_dict['time']
        self.timezone = json_dict['timezone']
        self.depth_unit = json_dict['depth unit']
        self.temperature_unit = json_dict['temperature unit']
        self.photo_count = json_dict['photos']
        # Looks like video count is probably wrong
        self.video_count = json_dict['videos']

    '''
    '''
    def set_modified(self, server_response: str):
        """
        FTP command to get the modified time of the camera file
        format MDTM <filename>
        returns 213 YYYYMMDDHHMMSS UTC

        :param server_response: str 213 YYYYMMDDHHMMSS
        :return: None
        """
        modified_time = server_response.split(' ')[1]
        parsed_time = datetime.datetime.strptime(modified_time + "+0000", "%Y%m%d%H%M%S%z")
        self.parsed_time = parsed_time


if __name__ == "__main__":
    camera = Camera()
    camera.set_modified('213 20221230061203')
