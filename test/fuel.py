import csv 
import sys
import datetime
def main():
    filename = "dump.csv"
    keep = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["name"] = clean_text(row["name"])
                row["age"] = clean_age(row["age"])
                row["city"] = clean_text(row["city"])
                row["signup_date"] = clean_date(row["signup_date"])
                row["score"] = clean_score(row["score"])

                if row in keep:
                    continue
                else:
                    keep.append(row)
            # print(keep)
    except FileNotFoundError:
        sys.exit(f"{filename} file not found")
    except KeyError as error:
         sys.exit(f"{error.args[0]} column is missing in {filename} ")
    # write part below  
    """filename2 = "cleaned_dump.csv"
    if keep:
        with open(filename2, "w",newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(keep[0]))
            writer.writeheader()
            writer.writerows(keep)
    else:
         sys.exit("No data found")"""

    

def clean_text(text):
     return " ".join(text.split()).title()
def clean_age(age):
    try:
        return int(age)
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
def extractor(date):
    date = date.strip()
    if "-" in date:
        try:
             if  len(date.split("-")) == 3:
                year,month,day = date.split("-")
                return int(year),int(month),int(day)
        except ValueError:
             return None
    if "/" in date:
       if  len(date.split("/")) == 3:
            day,month,year = date.split("/")
            try:
                return int(year),int(month), int(day)
            except ValueError:
                 return None
       else:
            return None
    parts = date.split()
    if  len(parts) == 3 and parts[0].title() in months:
        month,day,year = parts
        monthno = months.index(month.title()) + 1
        try:
            day,year = int(day), int(year)
            return year,monthno,day   
        except ValueError:
             return None
        
    else:
         return None
current_year = datetime.date.today().year
def clean_date(raw):
    hold = extractor(raw)
    if hold is None:
        return None
    year,month,day = hold
    if 1960 > year or current_year < year:
        return None 
    try:
        return datetime.date(year,month,day).isoformat()
    except ValueError:
        return None

def clean_score(score):
     try:
          return float(score)
     except ValueError:
          return None
       


if __name__ == "__main__":
    main()