from unittest.mock import patch

def mocked_foo():
    print("mocked_foo called")

@patch("module.foo", mocked_foo)
def test_me():
    from module import foo
    foo()

