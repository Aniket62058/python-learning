import zipfile

to_zip = ['./data/f1.txt', './data/f2.txt']


def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)


create_zip('./data/files.zip', to_zip, 'w')
