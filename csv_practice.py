import csv

# Exercise 2

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
print()


# Exercise 3

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(f"Header: {header}")
    print()

    for row in reader:
        print(row)
print()

# Exercise 4

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(f"Header: {header}")
    print()

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print()
print(f"Total Revenue: ${total_revenue:.2f}")
print()

# Exercise 5

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as cleaned_file:
        writer = csv.writer(cleaned_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                cleaned_count += 1

print()
print(f"Original Rows: {original_count}")
print(f"Cleaned Rows Written: {cleaned_count}")
print()

# Exercise 6

total_revenue = 0

print()
print("Sales Using DictReader:")
print()

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print()
print(f"Total Revenue: ${total_revenue:.2f}")
print()
# csv.reader is useful for simple CSV files when I know the column positions.
# csv.DictReader is better when I want to access columns by name instead of index.

# Exercise 7

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity

        sales_summary[product] = sales_summary.get(product, 0) + revenue

print()
print("Sales Summary by Product:")
print()

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")
print()

# Exercise 8

from datetime import datetime

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue += revenue

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print()
print(f"Run logged at: {timestamp}")
print(f"Total Revenue: ${total_revenue:.2f}")
print()