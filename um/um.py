import re

def main():
    print(count(input("Text: ")))


def count(s):
    # Use a regular expression to find the occurrences of "um" as a whole word
    pattern = r'\bum\b'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)

    # Return the count of matches
    return len(matches)


if __name__ == "__main__":
    main()
