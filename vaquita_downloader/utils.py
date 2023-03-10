import bisect
import datetime
from typing import TypedDict, Literal

ZERO = datetime.timedelta(0)
TEN_MINUTES = 60*10  # Seconds in 10 minutes


# A UTC class.
class UTC(datetime.tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


class LogBuffer:
    """
    This class holds on to the last 10 minutes of log rows
    """

    def __init__(self, oldest_time=TEN_MINUTES):
        self.items = []
        self.oldest_time = oldest_time

    def add_row(self, row):
        self._check_time(row)
        bisect.insort(self.items, row, key=lambda k: k["time"])

    def _check_time(self, row):
        while self.items[0] < int(row["time"]) - self.oldest_time:
            self.items.pop(0)


class MaxSizeBuffered(BaseException):
    pass


class MaxLogBuffer(LogBuffer):

    def __init__(self, oldest_time=TEN_MINUTES):
        super().__init__(oldest_time)

    def _check_time(self, row):
        if self.items[0] < int(row["time"]) - self.oldest_time:
            raise MaxSizeBuffered()


def sort_numeric_strings(items, prefix, suffix, key=lambda k: k):
    numbers = []

    for item in items:
        numbers.append(int(key(item).replace(prefix, '').replace(suffix, '')))

    numbers.sort()

    for number in numbers:
        yield f'{prefix}{number}{suffix}'


CameraInfo = TypedDict('CameraInfo', {
    "firmware": str,
    "id": str,
    "session": int,
    "time": int,
    "timezone": str,
    "depth unit": Literal['METER', 'FEET'],
    "temperature unit": Literal['CELSIUS', 'FAHRENHEIT'],
    "photos": int,
    "videos": int,
})


LogRow = TypedDict('LogRow', {
    "Time": int,
    "Temperature": float,
    "Depth": float,
    "Image/video-file": str,
    "Video tags": str,
    "BTLVL": int,
    "Mode": str,
    "Res": str,
    "FPS": int,
    "Overlay": str,
    "DCCWB": str,
    "EIS": str,
    "Autorec": str,
    "Wifi": str,
    "Sdcard": str,
    "Firmware": str,
    "Lat": float,
    "Lng": float,
    "Alt": float,
    "Salinity": float,
    "RDRP": float,
    "BDRP": float,
    "ISO8601": str,
}, total=False)
