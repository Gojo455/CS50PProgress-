months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        entry = input()
        if "/" in entry:
            month,day,year = entry.split("/")
            month,day = int(month), int(day)
            if 1 <= day <= 31 and 1 <= month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
        elif "," in entry:
            month, day, year = entry.split(" ")
            day = day.strip(",")
            month = month.title()
            if month in months and 1 <= day <= 31:
                    mon = months.index(month) + 1
                    print(f"{year}-{mon:02}-{day:02}")
                    break
            else:
                continue 
        else:
             break
    except ValueError:
         continue 