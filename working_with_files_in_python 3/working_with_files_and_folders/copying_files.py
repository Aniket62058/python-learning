import shutil


def copy_file(src, dest):
    shutil.copyfile(src, dest)


def copy_folder(src, dest):
    shutil.copytree(src, dest)


copy_file('copying_files.py', 'new_file.py')
copy_folder('../working_with_files_and_folders', '../new_folder')
