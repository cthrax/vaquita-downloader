from csv import DictReader

from vaquita_downloader import utils
from vaquita_downloader.camera_instance import Camera
from vaquita_downloader.utils import LogRow


class LogBatch:

    def __init__(self, camera: Camera):
        self.logs = []
        self.ten_min_buffer = utils.LogBuffer()
        self.dive_buffer = utils.MaxLogBuffer(oldest_time=60 * 80)  # 80 minutes for a dive
        self.dive_started = False
        self.dive_ended = True
        self.camera = camera

        # Meters or feet
        self.surface_depth = 2 if camera.depth_unit == 'METER' else 5

    def _end_dive(self):
        # Need to move the dive readings into a format
        # Need to be able to extract images and videos easily
        pass

    def _add_dive_row(self, logRow: LogRow, at_surface: bool):
        # This means we have already started a dive
        # Cases are:
        # 1. The dive buffer is full
        #    add_row and end_dive
        # 2. The dive is continuing
        #    add_row and continue dive
        # Additionally, there is book keeping for ending the dive
        #  Cases are:
        # 1. A reading was below the surface_depth
        #      Check 2 things:
        #      1. Is this the first reading below the surface_depth?
        #         If yes, mark the occurrence in surface_start_time
        #      2. Is this past 10 minutes of readings below the surface_depth
        #         If yes, end the dive
        # 2. A reading was above the surface_depth
        #    Clear the surface_start_time
        try:
            self.dive_buffer.add_row(logRow)
        except utils.MaxSizeBuffered:
            # We have filled a dive before getting 0 depth readings
            self.dive_started = False

        # Start surface interval starting after 10 minutes of less than surface_depth
        if int(logRow['Depth']) <= self.surface_depth:
            if not at_surface:
                surface_start_time = int(logRow['Time'])

            at_surface = True
        elif int(logRow['Depth']) >= self.surface_depth:
            # This condition is if we didn't hit 10 minutes at surface, restart counter
            at_surface = False

        return at_surface

    def add_csv(self, csv: DictReader):
        """
        :param csv: open csv.DictReader
        :return:
        """
        at_surface = False
        surface_start_time = None
        for line in csv:  # type: LogRow
            # Always keep a 10 minute buffer
            self.ten_min_buffer.add_row(line)

            # If we're presently recording a log
            if self.dive_started:
                at_surface = self._add_dive_row(line, at_surface)

