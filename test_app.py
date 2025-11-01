from app import add

def test_add():
    assert(add(2,3)) == 5

def test_add_2():
    assert(add(-5,-5)) == -10