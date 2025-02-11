

def favorite_books():
    # List of tuples,
    #   each tuple contains the book title and author
    books = [
        ("Ready Player One", "Ernest Cline"),
        ("Tales from the Gas Station: Volume 1", "Jack Townsend"),
        ("The Way of Kings", "Brandon Sanderson"),
        ("Fight Club", "Chuck Palahniuk"),
        ("13th Legion", "Dan Abnett")
    ]
    return books[:3] # [:3] is a slice to return the first 3 elements of a list


def student_database():
    # Dictionary of students, format is: "Name": Student ID (key: value)
    students = {
        "Rusty Shackleford": 9001,
        "Dale Gribble": 9002,
        "Tyler Durden": 99999999,
        "Samwise Gamgee": 42
    }
    return students


print("First 3 favorite books:", favorite_books())
print("Student database:", student_database())