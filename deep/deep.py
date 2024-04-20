months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split()
        day = day.rstrip(',')
        month = str(months.index(month) + 1).zfill(2)
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and year.isnumeric():
            print(f"{year}-{month}-{day}")
            break
    except (ValueError, IndexError):
        pass
