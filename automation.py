import os
import shutil

def backup_folder(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)


def run():
    backup_folder("data", "backup")


if __name__ == "__main__":
    run()
