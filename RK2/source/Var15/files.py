class File:
    def __init__(self, numb, name, size, dir_id):
        self.__file_id = numb
        self.__name = name
        self.__size = size
        self.__dir_id = dir_id

    @property
    def file_id(self):
        return self.__file_id

    @property
    def name(self):
        return self.__name

    @property
    def dir_id(self):
        return self.__dir_id

    @property
    def size(self):
        return self.__size

    def __repr__(self):
        return "ID - {}, name - {}, size - {}, directory - {}".format(
            self.__file_id, self.__name, self.__size, self.__dir_id
        )


class Directory:
    def __init__(self, numb, name):
        self.__dir_id = numb
        self.__name = name

    @property
    def dir_id(self):
        return self.__dir_id

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "Directory name - {}".format(self.__name)


class DirectoryFiles:
    def __init__(self, file_id, dir_id):
        self.__file_id = file_id
        self.__dir_id = dir_id

    @property
    def dir_id(self):
        return self.__dir_id

    @property
    def file_id(self):
        return self.__file_id
