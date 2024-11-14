# File Organizer Script

This Python script organizes files within a specified folder by categorizing them based on their file extensions. Each file is moved to a subfolder, such as Documents, Images, Scripts, Audio, Videos, or Uncategorized, to keep your directory tidy and organized.

## Project Overview

When run, this script scans a given folder, determines each file’s type by its extension, and organizes it accordingly. It also generates a summary, displaying the count of files organized in each category.

### Features

- **Automated Categorization**: The script classifies files into predefined categories based on extensions:
  - **Documents**: `.pdf`, `.docx`, `.txt`, `.xls`, `.xlsx`
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Scripts**: `.py`, `.js`, `.html`, `.css`, `.cpp`
  - **Audio**: `.mp3`, `.wav`, `.aac`
  - **Videos**: `.mp4`, `.mov`, `.avi`
  - **Uncategorized**: Any other file extensions.
  
- **Customizable Extensions**: You can add new file types or categories by modifying the script.

- **Summary Output**: After organizing, the script provides a count of files sorted into each category.

## Project Structure

This project includes:

- **`organize_files.py`**: The main script that categorizes and organizes files.

### How It Works

1. **File Iteration**: The script scans through each file in the specified folder.
2. **Category Detection**: Based on the file extension, the script assigns files to categories.
3. **Folder Creation and Sorting**: For each category, a new folder is created if it doesn’t already exist, and files are moved accordingly.
4. **Summary Report**: Outputs a summary showing the number of files moved to each category.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions for improvements, please open an issue or submit a pull request.

---

Keep your files organized with this simple, customizable Python tool!
