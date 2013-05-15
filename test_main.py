from main import make_pushbutton

def test_pushbutton():
    b = make_pushbutton()
    b.show()
    assert b is not None
