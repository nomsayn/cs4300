import task5

def test_favorite_books():
    books = task5.favorite_books()
    assert len(books) == 3 # test that only the first 3 books are returned
    assert books[0] == ("Ready Player One", "Ernest Cline")
    assert books[1] == ("Tales from the Gas Station: Volume 1", "Jack Townsend")
    assert books[2] == ("The Way of Kings", "Brandon Sanderson")

def test_student_database():
    students = task5.student_database()
    assert isinstance(students, dict)
    assert students["Rusty Shackleford"] == 9001
    assert students["Dale Gribble"] == 9002
    assert students["Tyler Durden"] == 99999999
    assert students["Samwise Gamgee"] == 42