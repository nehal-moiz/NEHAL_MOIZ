import sys

def main():
    check_commands()
    count_lines()

def check_commands():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def count_lines():
    try:
        with open(sys.argv[1], "r") as file:
            line_count = 0
            for line in file:
                if not line.lstrip().startswith("#") and not line.strip() == "":
                    line_count += 1

        print(line_count)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
