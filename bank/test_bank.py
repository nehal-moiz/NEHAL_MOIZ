from bank import value

def main():

    test_return_zero()

def test_return_zero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('Hello Gi') == 0

if __name__ == "__main__":
    main()
