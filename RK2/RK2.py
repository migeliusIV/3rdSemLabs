import pytest
from source.Var15.files import File
from source.Var15.files import Directory
from source.Var15.files import DirectoryFiles


# Main program test
def test_main():
    """
    here's nothing to testing, IMHO, just visual effects
    even i will rebuild RK1 main file, nothing but the two print-function
    wouldn't become
    """
    pass


# Classes testing
def test_file():
    numb = 0
    name = "test_one.txt"
    size = 16
    dir_id = 0
    file_obj = File(numb, name, size, dir_id)

    conditions = [
        lambda o: o.file_id == numb,
        lambda o: o.name == name,
        lambda o: o.size == size,
        lambda o: o.dir_id == dir_id,
    ]
    is_valid = all(cond(file_obj) for cond in conditions)
    assert is_valid


def test_dir():
    numb = 0
    name = "Boss"
    dir_obj = Directory(numb, name)

    conditions = [lambda o: o.dir_id == numb, lambda o: o.name == name]
    is_valid = all(cond(dir_obj) for cond in conditions)
    assert is_valid


def test_directs_file():
    file_id = 0
    dir_id = 0
    file_obj = DirectoryFiles(file_id, dir_id)

    conditions = [lambda o: o.file_id == file_id, lambda o: o.dir_id == dir_id]
    is_valid = all(cond(file_obj) for cond in conditions)
    assert is_valid
