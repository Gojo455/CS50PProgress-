import csv 
import sys
from clean import clean_score

def main():
    year_columns = []
    row_keep = []
    file = "electricity_access_percent.csv"
    with open(file) as file:
        for _ in range(4):
            next(file)
        reader = csv.DictReader(file)
        
        columns = reader.fieldnames
        for items in columns:
            if items.isdigit():
                year_columns.append(items)
       
        for rows in reader:
            for year in year_columns:
                rows[year] = clean_score(rows[year]) 
            row_keep.append(rows)
        latest_year = find_latest_year(year_columns, row_keep)

        
       
    write_file = "cleaned_EAP.csv"
    with open(write_file, "w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames = columns[:4]+ [latest_year], extrasaction="ignore" )
        writer.writeheader()
        writer.writerows(row_keep)


def find_latest_year(years, rows):
    for year in reversed(years):
        for row in rows:
            if row[year] is not None:
                return year
    return None
                
          

if __name__ == "__main__":
    main()
