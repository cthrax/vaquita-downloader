from vaquita_downloader import utils


class DirectoryListing:
    def __init__(self):
        self.buffer = []
        self.filenames = []

    def add_bytes(self, block: str):
        self.buffer.append(block)

    def assemble(self):
        blocks = ''.join(self.buffer)
        for line in blocks.split('\n'):
            cols = line.split()
            if len(cols) > 1:
                self.filenames.append(cols[-1])

    def sorted(self):
        return utils.sort_numeric_strings(self.filenames, 'LOG', '.csv')
