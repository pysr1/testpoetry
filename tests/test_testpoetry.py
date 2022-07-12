from testpoetry import __version__
from testpoetry.hello_world import hello_world


def test_version():
    assert __version__ == '0.1.0'

def test_hello_world() -> None:
    assert hello_world() == 'hello world!'
