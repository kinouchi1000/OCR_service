from _path import *
from db.repository import Repository


def test_get_test():
    ret = Repository.create_result()

    print(ret)

    Repository.update_result(ret.id, "test!", "image_path_test")

    ret2 = Repository.get_text(ret.id)

    print(ret2)


test_get_test()
