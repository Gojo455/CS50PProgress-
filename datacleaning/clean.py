import csv 
def main():
    with open("student.csv") as file:
        reader = csv.DictReader(file)
        seen = set()
        keep = []
        for item in reader:
            item["name"] = clean_text(item["name"])
            item["city"] = clean_text(item["city"])
            item["age"] = clean_age(item["age"])
            item["score"] = clean_score(item["score"])
            item["signup_date"] = clean_date(item["signup_date"])
            tuples = tuple(item.values())

            if item in keep:
                continue
            keep.append(item)
            
        for items in keep:   
            print(items)

            
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
    date = date.strip()
    if "-" in date:
        return date
    if "/" in date:
        day,month,year = date.split("/")
        return f"{year}-{int(month):02}-{int(day):02}"
    parts = date.split()
    if len(parts) == 3 and parts[0].title() in months:
        month,day,year = parts
        monthno = months.index(month.title()) + 1
        return f"{year}-{monthno:02}-{int(day):02}"
    return None
            


if __name__ == "__main__":
    main()
        