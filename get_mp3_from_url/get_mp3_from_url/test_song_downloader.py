"""Example of unittest file"""

import unittest
from pathlib import Path

from .song_downloader import download_songs, get_output_template


class TestDownloadSongs(unittest.TestCase):
    def test_download_songs_raise_if_batch_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            download_songs(
                Path("Not existing"), Path("/home/foo/downloads"), Path("/home/foo/.get_mp3_from_url/cache.txt")
            )

    def test_download_songs_raise_if_destination_folder_not_found(self):
        with self.assertRaises(FileNotFoundError):
            download_songs(Path(__file__), Path("not existing"), Path("/home/foo/.get_mp3_from_url/cache.txt"))

    def test_download_songs_raise_if_cache_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            download_songs(Path(__file__), Path(__file__).parent, Path("not existing"))


class TestGetOutputTemplate(unittest.TestCase):
    def test_get_output_template(self):
        destination_path = Path(Path.home() / "Downloads" / "mp3_from_url")
        expected_template = str(destination_path) + "/%(title)s.%(ext)s"
        self.assertEqual(expected_template, get_output_template(destination_path))
