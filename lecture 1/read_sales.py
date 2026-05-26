import csv

total_revenue = 0

with open('sales.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    for row in reader:
        revenue = int(row[1])
        total_revenue += revenue

print(f"Total revenue: {total_revenue}")
