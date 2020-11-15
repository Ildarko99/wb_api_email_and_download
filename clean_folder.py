import os, shutil
from pathlib import Path

def clean_folder():
    import os, shutil
    folder = 'files'
    print(folder)
    for filename in os.listdir(folder):
        print(filename)
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

if '__name__' == '__main__':
    clean_folder()