from nox_demo.main import make_upper


def test_make_upper():
    result = make_upper("hello world")
    assert result == "HELLO WORLD"
