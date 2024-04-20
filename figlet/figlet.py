import sys
from pyfiglet import Figlet

def main():
    if len(sys.argv) == 1:
        isRandomFont = True
    elif len(sys.argv) == 3 and (sys.argv[1] in ["-f", "--font"]):
        isRandomFont = False
        selected_font = sys.argv[2]
    else:
        print("Usage: python figlet.py [(-f | --font) FONT_NAME]")
        sys.exit(1)

    figlet = Figlet(font='random' if isRandomFont else selected_font)

    text = input("Enter text: ")

    output = figlet.renderText(text)
    print(output)

if __name__ == "__main__":
    main()
