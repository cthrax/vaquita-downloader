import pytest

from vaquita_downloader.directory_listing import DirectoryListing
from vaquita_downloader.tests.fixtures import directory_listings_examples


class TestDirectoryListing:

    @pytest.mark.parametrize(
        'example_data,example_expected',
        [pytest.param(*directory_listings_examples.BASIC_EXAMPLE, id='BASIC'),
         pytest.param(*directory_listings_examples.REAL_EXAMPLE, id='REAL')])
    def test_listing(self, example_data: str, example_expected):
        d = DirectoryListing()
        d.add_bytes(example_data)
        d.assemble()
        assert d.filenames == example_expected

    @pytest.mark.parametrize(
        'example_data,example_expected',
        [pytest.param(*directory_listings_examples.BASIC_SORTED_EXAMPLE, id='BASIC_SORTED')])
    def test_sorting(self, example_data: str, example_expected):
        d = DirectoryListing()
        d.add_bytes(example_data)
        d.assemble()
        assert list(d.sorted()) == example_expected


