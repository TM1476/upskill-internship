import os
import shutil

def organize_files(path):
    try:
        files = os.listdir(path)

        file_types = {
            "Images": [".jpg", ".png", ".jpeg"],
            "Documents": [".pdf", ".txt", ".docx"],
            "Videos": [".mp4", ".mkv"]
        }

        for folder in file_types:
            os.makedirs(os.path.join(path, folder), exist_ok=True)

        os.makedirs(os.path.join(path, "Others"), exist_ok=True)

        for file in files:
            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):
                moved = False

                for folder, extensions in file_types.items():
                    if any(file.lower().endswith(ext) for ext in extensions):
                        destination = os.path.join(path, folder, file)

                        if os.path.exists(destination):
                            destination = os.path.join(path, folder, "copy_" + file)

                        shutil.move(file_path, destination)
                        print(f"Moved {file} → {folder}")
                        moved = True
                        break

                if not moved:
                    destination = os.path.join(path, "Others", file)
                    shutil.move(file_path, destination)
                    print(f"Moved {file} → Others")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    folder_path = input("Enter folder path: ")
    organize_files(folder_path)
