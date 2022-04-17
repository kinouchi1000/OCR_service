from _path import *
from db.repository import Repository


def test_get_test():
    ret = Repository.create_text("test!", ".png")

    print(ret)

    ret2 = Repository.get_text(ret.id)

    print(ret2[0].id)


test_get_test()
