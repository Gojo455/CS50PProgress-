years = ["2015", "2016", "2017"]
rows = [
    {"2015": 5.0, "2016": 6.0, "2017": None},
    {"2015": None, "2016": 0.0, "2017": None},
]
ear = []
for year in reversed(years):
    for row in rows:
        if row[year]:
            ear.append(year)
            break
        
        
print(ear)