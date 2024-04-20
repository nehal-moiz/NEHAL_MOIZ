def main():
    fractions = input("Fractions: ")
    fractions_converted = convert(fractions)
    output = gauge(fractions_converted)
    print(output)

def convert(fractions):
    while True:
        try:
            numerator, denominator = fractions.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)

            if new_denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero")

            f = new_numerator / new_denominator

            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fractions = input("Fractions: ")
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter fractions in the format 'numerator/denominator'.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
