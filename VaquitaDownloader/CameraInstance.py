import datetime
import json

from VaquitaDownloader.utils import UTC

INFO_FILE_NAME = '.camera.json'

class Camera:

    def __init__(self, json_bytes=None):
        if json_bytes is not None:
            string = str(json_bytes, 'utf-8')
            self.set_from_json(json.loads(str(json_bytes, 'utf-8')))


    '''
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
    '''
    def set_from_json(self, json_dict):
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
        FTP command to get the modified time of the camera file
        format MDTM <filename>
        returns 213 YYYYMMDDHHMMSS UTC
    '''
    def set_modified(self, server_response):
        print(server_response)
        modified_time = server_response.split(' ')[1]
        parsed_time = datetime.datetime.strptime(modified_time + "+0000", "%Y%m%d%H%M%S%z")
        print(parsed_time.tzinfo)


if __name__ == "__main__":
    camera = Camera()
    camera.set_modified('213 20221230061203')
