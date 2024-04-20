import numb3rs

def test_valid_ipv4():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True

def test_invalid_ipv4():
    assert numb3rs.validate("512.512.512.512") == False
    assert numb3rs.validate("1.2.3.1000") == False
    assert numb3rs.validate("cat") == False

def test_validate_function():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("512.512.512.512") == False
    assert numb3rs.validate("1.2.3.1000") == False
    assert numb3rs.validate("cat") == False

if __name__ == "__main__":
    # Use pytest to discover and run the tests
    import pytest
    pytest.main()
