from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True

def test_invalid_range():
    assert validate("256.255.255.255") == False
    assert validate("192.300.1.1") == False
    assert validate("10.10.10.10.10") == False

def test_invalid_format():
    assert validate("cat") == False
    assert validate("8.8.8") == False

def test_leading_zeros():
    assert validate("000.001.010.100") == False