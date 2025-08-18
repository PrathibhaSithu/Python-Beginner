"""
Simple file organizer.
- Scans a folder
- Moves files into subfolders by extension (e.g., .jpg -> Images)
- Skips conflicts by auto-renaming
- Creates folders if missing
"""

from pathlib import Path
import shutil

# Map extensions to target folder names
EXT_MAP = {
    # Images
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".webp": "Images", ".svg": "Images",
    # Videos
    ".mp4": "Videos", ".mkv": "Videos", ".mov": "Videos", ".avi": "Videos",
    # Audio
    ".mp3": "Audio", ".wav": "Audio", ".m4a": "Audio", ".flac": "Audio",
    # Documents
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents", ".pptx": "Documents",
    ".txt": "Documents", ".md": "Documents", ".rtf": "Documents",
    # Code
    ".py": "Code", ".js": "Code", ".ts": "Code", ".html": "Code", ".css": "Code", ".json": "Code", ".yml": "Code", ".yaml": "Code",
    # Archives
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives", ".tar": "Archives", ".gz": "Archives",
    # Installers
    ".exe": "Installers", ".msi": "Installers", ".dmg": "Installers", ".apk": "Installers"
}


def safe_move(src: Path, dest_dir: Path) -> Path:
    """
    Move src into dest_dir, avoiding name collisions by appending a counter.
    Returns the final destination path.
    """
    dest_dir.mkdir(parents=True, exist_ok=True)  # ensure target exists
    dest = dest_dir / src.name                   # candidate destination path

    if not dest.exists():                        # if no conflict, move directly
        return src.rename(dest)

    # split name into base and extension
    stem, suffix = dest.stem, dest.suffix
    counter = 1                                  # start counter for duplicates
    while True:                                  # loop until a free name is found
        candidate = dest_dir / f"{stem} ({counter}){suffix}"
        if not candidate.exists():               # if candidate is free, move and break
            return src.rename(candidate)
        counter += 1


def organize_folder(root: str) -> None:
    """
    Organize files in 'root' directory by extension using EXT_MAP.
    Files with unknown extensions go to 'Others'.
    Folders are left in place.
    """
    base = Path(root).expanduser().resolve(
    )     # normalize user path (handles ~)
    if not base.is_dir():                        # ensure the path is a directory
        raise NotADirectoryError(f"Not a directory: {base}")

    for item in base.iterdir():                  # iterate over items in the folder
        if item.is_dir():                        # skip subfolders
            continue

        ext = item.suffix.lower()                # get file extension in lowercase
        # pick target folder or Others
        target_name = EXT_MAP.get(ext, "Others")
        target_dir = base / target_name          # compute full target folder path

        try:
            # move safely with collision handling
            safe_move(item, target_dir)
        except PermissionError:
            # handle locked files gracefully
            print(f"Skipped (locked): {item}")
        except OSError:
            # handle cross-device move by copying then deleting if needed
            temp_dest = target_dir / item.name
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, temp_dest)
            item.unlink(missing_ok=True)


if __name__ == "__main__":
    # Change this to the folder you want to organize, e.g., r"D:\Downloads"
    # uses a relative path by default
    organize_folder(r"./Downloads")
