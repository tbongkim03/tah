from tah.cli import hello_msg

def test_hello():
    m = hello_msg()
    assert m == "hello"
