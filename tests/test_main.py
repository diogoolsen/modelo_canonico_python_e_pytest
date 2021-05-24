
# from src import __main__
import src


def test_main_ok():
    assert src.__main__.var == '__main__'
