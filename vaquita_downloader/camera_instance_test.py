from datetime import datetime

from vaquita_downloader import utils
from vaquita_downloader.camera_instance import Camera


class TestCameraInstance:

    def test_parse_date(self):
        camera = Camera()
        camera.set_modified('213 20221230061203')
        assert camera.parsed_time == datetime(year=2022, month=12, day=30, hour=6, minute=12, second=3, tzinfo=utils.UTC())
