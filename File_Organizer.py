import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path")
        return

    summary = {
        "Documents": 0,
        "Images": 0,
        "Scripts": 0,
        "Audio": 0,
        "Videos": 0,
        "Uncategorized": 0
    }


    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)  
        if os.path.isfile(file_path):  
            ext = os.path.splitext(filename)[1].lower()  

            
            if ext in [".pdf", ".docx", ".txt", ".xls", ".xlsx"]:
                category = "Documents"
            elif ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
                category = "Images"
            elif ext in [".py", ".js", ".html", ".css", ".cpp"]:
                category = "Scripts"
            elif ext in [".mp3", ".wav", ".aac"]:
                category = "Audio"
            elif ext in [".mp4", ".mov", ".avi"]:
                category = "Videos"
            else:
                category = "Uncategorized"

           
            target_folder = os.path.join(folder_path, category)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(file_path, target_folder)
            summary[category] += 1

   
    print("\nSummary of Files Organized:")
    for category, count in summary.items():
        print(f"{category}: {count}")


folder_path = input("Enter the folder path to organize: ").strip()
organize_files("D:\\File Organizer")
