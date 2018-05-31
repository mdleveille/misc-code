import os


def rename_files():
    file_list = os.listdir(path='/Users/mleveille/misc-code/udacity/prank')
    print(file_list)

    working_dir = os.getcwd()
    print(working_dir)
    os.chdir('/Users/mleveille/misc-code/udacity/prank')

    for file in file_list:
        os.rename(file, file.lstrip('0123456789'))
    os.chdir(working_dir)
    print(file_list)


rename_files()
