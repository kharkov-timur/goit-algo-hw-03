import os
import shutil
import sys


def copy_files_recursively(source_dir, target_dir):
    os.makedirs(target_dir, exist_ok=True)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        if os.path.isdir(source_path):
            copy_files_recursively(source_path, target_dir)
        else:
            extension = os.path.splitext(item)[1][1:].lower()
            extension_dir = os.path.join(target_dir, extension)
            os.makedirs(extension_dir, exist_ok=True)

            target_path = os.path.join(extension_dir, item)
            shutil.copy2(source_path, target_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: script.py <source_dir> [<target_dir>]")
        sys.exit(1)

    source_dir = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(source_dir, "dist")

    try:
        copy_files_recursively(source_dir, target_dir)
        print(f"Файли успішно скопійовано до {target_dir}")
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")
