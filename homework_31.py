from contextlib import contextmanager
import os

#Task 1
#створити контекст менеджер, якому можна передати ім'я файла і вміст. На вході він його створить з вмістом

class OpenFile:
    def __init__(self, filename, mode, info_in_file):
        self.filename = filename
        self.mode = mode
        self.info_in_file = info_in_file

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.file.write(self.info_in_file)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('homework.txt', 'w', 'hello! This is a homework test file') as f:
    print('Done')


@contextmanager
def create_file(filename, mode, info_in_file):
    f = open(filename, mode)
    f.write(info_in_file)
    yield f
    f.close()

#with create_file('homework_31.txt', 'w', 'hello! This is a second homework test file') as f:
    #print('File was created')

#Task 2
#створити контекст менеджер, якому можна передати ім'я папки і назви файлів.На вході він створить папку з усіма файлами

class Open_Directory:

    def __init__(self, name_of_dir, *args):
        self.name_of_dir = name_of_dir
        self.name_of_files = args
        self.cwd = os.getcwd()
        self.index = 0

    def __enter__(self):
        if not os.path.isdir(self.name_of_dir):
            os.mkdir(self.name_of_dir)
            os.chdir(self.name_of_dir)
            for i in self.name_of_files:
                self.file = open(self.name_of_files[self.index] + '.txt', mode="w")
                self.file.close()
                self.index += 1
        else:
            print('Impossible to create file')

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.cwd)

#with Open_Directory('new_directory', "first", "second"):
    #print('Done')

@contextmanager
def create_directory(name_of_dir, *args):
    name_of_files = args
    cwd = os.getcwd()
    index = 0
    if not os.path.isdir(name_of_dir):
        os.mkdir(name_of_dir)
        os.chdir(name_of_dir)
        for i in name_of_files:
            f = open(name_of_files[index] + '.txt', mode="w")
            f.close()
            index += 1
    else:
        print('Impossible to create file')
    yield
    os.chdir(cwd)


with create_directory('new_directory', "first", "second"):
    print('Done')
