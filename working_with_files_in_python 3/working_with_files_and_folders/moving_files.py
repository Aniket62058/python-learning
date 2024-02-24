import shutil


def move_file(src, dest):
    shutil.move(src, dest)


# move_file('__init__.py','init.py')
# move_file('init.py','__init__.py')
# move_file('../finding_files','../new_package')
move_file('../new_package', '../finding_files')
