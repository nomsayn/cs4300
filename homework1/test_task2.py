import task2

def test_get_int():
    # isinstance() returns True if the specified object is of the specified type
    assert isinstance(task2.get_int(), int)

def test_get_float():
    assert isinstance(task2.get_float(), float)

def test_get_string():
    assert isinstance(task2.get_string(), str)

def test_get_bool():
    assert isinstance(task2.get_bool(), bool)

def test_get_list():
    assert isinstance(task2.get_list(), list)