import json
import pathlib
from typing import Callable
from unittest.mock import patch, MagicMock, call

import pytest

from vaquita_downloader import camera_instance
from vaquita_downloader.camera_session import CameraSession
from vaquita_downloader.tests.fixtures import camera_info_examples, logs


@pytest.fixture(scope='function')
def mock_ftp():
    with patch('ftplib.FTP', autospec=True) as mock_ftp_constructor:
        with patch.object(pathlib.Path, 'mkdir') as mock_path_constructor:
            yield mock_ftp_constructor.return_value


class TestCameraSession:
    def test_connect_to_server(self, mock_ftp: MagicMock):
        camera_session = CameraSession()
        camera_session.connect_to_server()
        mock_ftp.login.assert_called_once_with(camera_session.username, camera_session.password)
        calls = []
        for arg in ['TYPE I', 'SYST', 'FEAT', 'OPTS UTF8 ON']:
            calls.append(call(arg))
        mock_ftp.sendcmd.assert_has_calls(calls, any_order=False)
        mock_ftp.set_pasv.assert_called_once_with(True)

    def test_retr_camera_info(self, mock_ftp):
        camera_session = CameraSession()
        retrieved_binary = False

        # Could expose the value to be dumped, but easier to define inline
        def mock_retrbinary(cmd, callback: Callable[[bytes], None]):
            nonlocal retrieved_binary
            assert cmd == f'RETR {camera_instance.INFO_FILE_NAME}'
            callback(json.dumps(camera_info_examples.BASIC).encode('UTF-8'))
            retrieved_binary = True

        mock_ftp.retrbinary = mock_retrbinary
        mock_ftp.sendcmd.return_value = '213 20221230061203'
        camera_session.retr_camera_info(mock_ftp)
        assert retrieved_binary is True
        mock_ftp.sendcmd.assert_called_once_with(f'MDTM {camera_instance.INFO_FILE_NAME}')

    def test_import_new_media(self):
        camera_session = CameraSession(cache_dir=pathlib.Path(logs.__file__).parent.absolute())
        camera_session.import_new_media()
