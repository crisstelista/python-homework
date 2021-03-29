import csv

menu_file_path = "menu_data.csv"
sales_file_path = "sales_data.csv"

output_file = "output.txt"

menu_data = {}
sales_data = []

with open(menu_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        menu_data[row[0]] = [row[1], row[2], row[3], row[4]]
with open(sales_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

    for row in csvreader:
        sales_data.append([row[0], row[1], row[2], row[3], row[4]])

report = {}

for sale in sales_data:

    quantity = int(sale[3])
    sales_item = sale[4]

    if report.get(sales_item) == None:
        report[sales_item] = {"01-count": 0,
                              "02-revenue": 0,
                              "03-cogs": 0,
                              "04-profit": 0}
    menu = menu_data[sales_item]
    if(menu_data['spicy miso ramen']):
        if menu != None:
            cost = float(menu[3])
            price = float(menu[2])
            profit = price - cost

            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        else:
            print(f'{sales_item} does not contains data')
    else:
        continue

with open(output_file, "w") as file:
    for sales_item in report:
        print(f'{sales_item} : {report[sales_item]}')
        file.write(f'{sales_item} : {report[sales_item]}\n')