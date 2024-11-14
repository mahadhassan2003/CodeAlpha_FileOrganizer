```markdown
# File Organizer Script

This Python script organizes files within a specified folder by categorizing them into folders such as Documents, Images, Scripts, Audio, Videos, and Uncategorized based on their file extensions. It also provides a summary of the files organized in each category.

## Features

- **Categorizes files**: Automatically moves files into folders based on file extensions:
  - **Documents**: `.pdf`, `.docx`, `.txt`, `.xls`, `.xlsx`
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Scripts**: `.py`, `.js`, `.html`, `.css`, `.cpp`
  - **Audio**: `.mp3`, `.wav`, `.aac`
  - **Videos**: `.mp4`, `.mov`, `.avi`
  - **Uncategorized**: Any other file extensions
- **Summary output**: Displays a count of files organized into each category.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Clone or download this repository.
2. Update the `folder_path` variable with the directory you want to organize, or input it when prompted.
3. Run the script:

   ```bash
   python organize_files.py
   ```

4. Enter the full path to the folder you want to organize when prompted, or update the default path in the code (`folder_path = "D:\\File Organizer"`).

### Example

```
Enter the folder path to organize: D:\MyFiles
Summary of Files Organized:
Documents: 5
Images: 10
Scripts: 2
Audio: 3
Videos: 1
Uncategorized: 4
```

## Customization

You can update the file extensions or add new categories by editing the `ext` lists in the script.

## Author

*Mahad Hassan*

---

This is a simple organizational tool to keep your files tidy. Contributions and suggestions are welcome!
```
