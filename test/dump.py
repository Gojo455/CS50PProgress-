import sys
import csv 
def main():
    keep = []
    try:
        with open("dump.csv") as file: 
            reader = csv.DictReader(file)
            for item in reader:
                item["name"] = clean_text(item["name"])
                item["city"] = clean_text(item["city"])
                item["age"] = clean_age(item["age"])
                item["score"] = clean_score(item["score"])
                item["signup_date"] = clean_date(item["signup_date"])
                if item in keep:
                    continue
                keep.append(item)
    except FileNotFoundError:
                sys.exit("File not found")
    if not keep:
        print(f"no data found in dump.csv", file = sys.stderr)
        sys.exit(1)

    else:
        with open("dump_student.csv", "w", newline="") as note:
                writer = csv.DictWriter(note, fieldnames= list(keep[0]))
                writer.writeheader()
                writer.writerows(keep) 

            
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
        
