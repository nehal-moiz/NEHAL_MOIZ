import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Define a regular expression pattern to match YouTube URLs in src attribute
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'

    # Use re.search to find the pattern in the input string
    match = re.search(pattern, s)

    # If a match is found, return the youtu.be URL, else return None
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()
