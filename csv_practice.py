import csv

# Exercise 2: Read and Print Raw Rows

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
print()


# Exercise 3: Skip the Header

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(f"Header: {header}")
    print()

    for row in reader:
        print(row)
print()

# Exercise 4: Calculate Total Revenue

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

# Exercise 5: Filter and Write CSV

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