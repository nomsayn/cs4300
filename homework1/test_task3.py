import task3

def test_check_pos_or_neg():
    assert task3.check_pos_or_neg(45) == "Positive"
    assert task3.check_pos_or_neg(-23) == "Negative"
    assert task3.check_pos_or_neg(0) == "Zero"

def test_first_10_primes():
    assert task3.first_10_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_100_nums():
    assert task3.sum_100_nums() == 5050 # sum of 1 to 100 is 5050
