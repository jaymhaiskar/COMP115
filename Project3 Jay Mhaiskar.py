"""
Author: Jay Mhaiskar 
Date: November 14, 2023
COMP 115 Project 3 Appendix A

"""


with open("BC_Census_2016_data.csv", "r") as file:
    lines = file.readlines()

    column_titles = lines[0].strip().split(",")
    data = [line.strip().split(",") for line in lines[1:]]

print("Task 1:")
print("Community Health Service Areas (CHSAs) where shelt_rent_30plus_rate > 50%:")
for row in data:
    if float(row[column_titles.index("shelt_rent_30plus_rate")]) > 50:
        print(row[column_titles.index("chsa")])


print("\nTask 2:")

pha_rates = {
    "Fraser": [],
    "Interior": [],
    "Northern": [],
    "Vancouver Coastal": [],
    "Vancouver Island": [],
}

for row in data:
    pha = row[column_titles.index("pha")]
    rate = float(row[column_titles.index("shelt_rent_subsidized_rate")])
    pha_rates[pha].append(rate)


for pha, rates in pha_rates.items():
    if rates:
        avg_rate = sum(rates) / len(rates)
        print(f"Average shelter subsidization rate in {pha} region: {avg_rate:.2f}")
    else:
        print(f"No data available for {pha} region")
