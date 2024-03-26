"""Utility functions to download mp3 from url."""
from pathlib import Path

def download_songs(batch_file_path:Path,destination_folder:Path,already_downloaded_list_file_path=Path) ->None :
    """Download songs listed by url in batch_file_path and put them in destination folder.

    Args:
        batch_file_path (Path): path to the batch file 
        destination_folder (Path): path to the destination folder
        already_downloaded_list_file_path (Path): path to the cache file 
    """
    for required_file in [batch_file_path,already_downloaded_list_file_path]:
        if not required_file.exists():
            raise FileNotFoundError(f"File not found: {required_file}")
    if not destination_folder.exists():
        raise FileNotFoundError(f"Folder not found: {destination_folder}")

    raise NotImplementedError