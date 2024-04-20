def main():
     fractions = input("Fractions: ")
     fractions_converted = convert(fractions)
     output = gauge(fractions_converted)
     print(output)



def convert(fractions):

while True:
     try:
          numerator , denominator = fuel.split("/")

          new_numerator = int(numerator)
          new_denominator = int(denominator)

          f = new_numerator / new_denominator
          if f <= 1:
               p = int(f * 100)
               return p
          else:
               fraction = input("Fractions: ")
               pass
     except (ValueError, ZeroDivisionError):
         raise

def gauge(percentage):

    if percentage <= 1:
         return "E"

     elif percentage >= 99:
         return "F"

    else:
         return str(percentage) + %


if __name__ == "__main__":
    main()
