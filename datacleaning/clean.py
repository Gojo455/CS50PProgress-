import csv 
def main():
    with open("student.csv") as file:
        reader = csv.DictReader(file)
        for item in reader:
            item["name"] = clean_text(item["name"])
            item["city"] = clean_text(item["city"])
            item["age"] = clean_age(item["age"])
            item["score"] = clean_score(item["score"])
            item["signup_date"] = clean_date(item["signup_date"])
            print(item)
def clean_text(text):
   return " ".join(text.split()).title()
def clean_age(age):
    try:
        return int(age)
    except ValueError:
        return None
def clean_score(score):
    try:
        return float(score)
    except ValueError:
        return None
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
def clean_date(date):

    for entry in date.split():
        if entry in months:
            month, day,year = date.split()
            monthno = months.index(month) + 1
            return f"{year}-{monthno}-{day}"
        elif "/" in date:
            day,month,year = date.split("/")
            return f"{year}-{month}-{day}"
        else:
            return date
            


if __name__ == "__main__":
    main()
        