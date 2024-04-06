"""Utility functions to download mp3 from url."""

import logging
from pathlib import Path

import yt_dlp

logging.basicConfig(level=logging.INFO)


YT_DL_OPTIONS = {
    "nooverwrites": True,
    "download_archive": "",
    "outtmpl": "",
    "writethumbnail": True,
    "noplaylist": True,
    "keepvideo": False,
    "extract_flat": True,
    "ignoreerrors": True,  # Ignore errors during extraction
    "skip_download": True,  # Skip downloading if extraction fails
    "youtube_include_dash_manifest": False,  # Do not include DASH manifests (if possible)
    "verbose": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",  # Extract audio
            "preferredcodec": "mp3",  # Convert to MP3
            "preferredquality": "192",  # Preferred quality for MP3
        }
    ],
}


def get_output_template(destination_folder: Path) -> str:
    """Create output template of youtube-dl being given the destination folder.

    Args:
        destination_folder (Path): folder where song should be recorded
    """
    return str(destination_folder) + r"/%(title)s.%(ext)s"


def download_songs(batch_file_path: Path, destination_folder: Path, already_downloaded_list_file_path=Path) -> None:
    """Download songs listed by url in batch_file_path and put them in destination folder.

    Args:
        batch_file_path (Path): path to the batch file
        destination_folder (Path): path to the destination folder
        already_downloaded_list_file_path (Path): path to the cache file. Will create one if none.
    """
    if not batch_file_path.exists():
        raise FileNotFoundError(f"File not found: {batch_file_path}")
    if not destination_folder.exists():
        raise FileNotFoundError(f"Folder not found: {destination_folder}")
    if not already_downloaded_list_file_path.exists():
        logging.warning("Cache file not found %s. Will create one", str(already_downloaded_list_file_path))

    yt_dlp_options = YT_DL_OPTIONS
    yt_dlp_options["download_archive"] = str(already_downloaded_list_file_path)
    yt_dlp_options["outtmpl"] = get_output_template(destination_folder)

    # pylint: disable=(consider-using-with)
    url_list = [line.rstrip("\n") for line in open(str(batch_file_path), encoding="utf-8")]

    with yt_dlp.YoutubeDL(yt_dlp_options) as youtube_downloader:
        for url in url_list:
            logging.info("Now downloading: %s", url)
            youtube_downloader.download([url])
