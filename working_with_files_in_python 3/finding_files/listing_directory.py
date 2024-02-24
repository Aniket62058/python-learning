import os


def list_dir(fld_path):
    for item in os.listdir(fld_path):
        print(item)


# list_dir('../finding_files')
list_dir('../../Fundamentals')
