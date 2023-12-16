# File Concatenator Script

## Purpose:

The File Concatenator Script is a utility script for processing and displaying files in a directory, allowing exclusions based on filename.

## Usage:

- **Linux (tree.sh):**
  ```shell
  bash tree.sh /path/to/directory -e file1 file2
  ```

- **Windows (tree.bat):**
  ```shell
  tree.bat /path/to/directory -e file1 file2
  ```

## Flags:

- `path`: Directory path to process.
- `-e, --exclude [EXCLUDE_FILES ...]`: (Optional) List of files to exclude.
