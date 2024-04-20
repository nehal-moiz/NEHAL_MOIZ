from twttr import shorten

def main():
    test_upper_lower_cases()


def test_upper_lower_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('!?.,') == '!?.,'
    assert shorten('1234') == '1234'
    assert shorten("Hello") == "Hll"
    assert shorten("aeiouAEIOU") == ""
    assert shorten("Python") == "Pythn"
    assert shorten("Quick brown fox") == "Qck brwn fx"
    assert shorten("12345") == "12345"


if __name__ == "__main":
    main()
