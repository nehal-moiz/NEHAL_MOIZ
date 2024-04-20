def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60.0

def main():
    answer = input("What time is it? ")
    time = convert(answer)

    if 7.0 <= time <= 8.0:
        print("Breakfast time")

    if 12.0 <= time <= 13.0:
        print("Lunch time")

    if 18.0 <= time <= 19.0:
        print("Dinner time")

if __name__ == "__main__":
    main()
