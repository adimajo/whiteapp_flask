import sys
sys.path.append("whiteapp")


def test_whiteapp():
    from whiteapp import __version__
    from whiteapp.wsgi import app
