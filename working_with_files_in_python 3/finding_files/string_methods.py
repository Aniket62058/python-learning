import os


def ends_with(fld_path, search):
    for file in os.listdir(fld_path):
        if file.endswith(search):
            print(file)


def starts_with(fld_path, search):
    for file in os.listdir(fld_path):
        if file.startswith(search):
            print(file)


# ends_with('../../Fundamentals','.py')
starts_with('../../Fundamentals', 'e')
